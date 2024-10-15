# SNMP MIB module (BSUCLK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BSUCLK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:43 2024
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

(bsu,) = mibBuilder.importSymbols(
    "ANIROOT-MIB",
    "bsu")

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

aniBsuClock = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 3, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _AniBsuClkSntpTimeZone_Type(DisplayString):
    """Custom type aniBsuClkSntpTimeZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_AniBsuClkSntpTimeZone_Type.__name__ = "DisplayString"
_AniBsuClkSntpTimeZone_Object = MibScalar
aniBsuClkSntpTimeZone = _AniBsuClkSntpTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 4, 1),
    _AniBsuClkSntpTimeZone_Type()
)
aniBsuClkSntpTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniBsuClkSntpTimeZone.setStatus("current")


class _AniBsuClkSntpDstEnable_Type(Integer32):
    """Custom type aniBsuClkSntpDstEnable based on Integer32"""
    defaultValue = 2

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


_AniBsuClkSntpDstEnable_Type.__name__ = "Integer32"
_AniBsuClkSntpDstEnable_Object = MibScalar
aniBsuClkSntpDstEnable = _AniBsuClkSntpDstEnable_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 4, 2),
    _AniBsuClkSntpDstEnable_Type()
)
aniBsuClkSntpDstEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniBsuClkSntpDstEnable.setStatus("current")


class _AniBsuClkSntpDstStart_Type(DisplayString):
    """Custom type aniBsuClkSntpDstStart based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_AniBsuClkSntpDstStart_Type.__name__ = "DisplayString"
_AniBsuClkSntpDstStart_Object = MibScalar
aniBsuClkSntpDstStart = _AniBsuClkSntpDstStart_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 4, 3),
    _AniBsuClkSntpDstStart_Type()
)
aniBsuClkSntpDstStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniBsuClkSntpDstStart.setStatus("current")


class _AniBsuClkSntpDstEnd_Type(DisplayString):
    """Custom type aniBsuClkSntpDstEnd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_AniBsuClkSntpDstEnd_Type.__name__ = "DisplayString"
_AniBsuClkSntpDstEnd_Object = MibScalar
aniBsuClkSntpDstEnd = _AniBsuClkSntpDstEnd_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 4, 4),
    _AniBsuClkSntpDstEnd_Type()
)
aniBsuClkSntpDstEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniBsuClkSntpDstEnd.setStatus("current")


class _AniBsuClkSntpEnable_Type(Integer32):
    """Custom type aniBsuClkSntpEnable based on Integer32"""
    defaultValue = 1

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


_AniBsuClkSntpEnable_Type.__name__ = "Integer32"
_AniBsuClkSntpEnable_Object = MibScalar
aniBsuClkSntpEnable = _AniBsuClkSntpEnable_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 4, 5),
    _AniBsuClkSntpEnable_Type()
)
aniBsuClkSntpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniBsuClkSntpEnable.setStatus("current")


class _AniBsuClkManualTime_Type(DisplayString):
    """Custom type aniBsuClkManualTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_AniBsuClkManualTime_Type.__name__ = "DisplayString"
_AniBsuClkManualTime_Object = MibScalar
aniBsuClkManualTime = _AniBsuClkManualTime_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 4, 6),
    _AniBsuClkManualTime_Type()
)
aniBsuClkManualTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniBsuClkManualTime.setStatus("current")


class _AniBsuClkCurrentTime_Type(DisplayString):
    """Custom type aniBsuClkCurrentTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_AniBsuClkCurrentTime_Type.__name__ = "DisplayString"
_AniBsuClkCurrentTime_Object = MibScalar
aniBsuClkCurrentTime = _AniBsuClkCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 4, 7),
    _AniBsuClkCurrentTime_Type()
)
aniBsuClkCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuClkCurrentTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BSUCLK-MIB",
    **{"aniBsuClock": aniBsuClock,
       "aniBsuClkSntpTimeZone": aniBsuClkSntpTimeZone,
       "aniBsuClkSntpDstEnable": aniBsuClkSntpDstEnable,
       "aniBsuClkSntpDstStart": aniBsuClkSntpDstStart,
       "aniBsuClkSntpDstEnd": aniBsuClkSntpDstEnd,
       "aniBsuClkSntpEnable": aniBsuClkSntpEnable,
       "aniBsuClkManualTime": aniBsuClkManualTime,
       "aniBsuClkCurrentTime": aniBsuClkCurrentTime}
)
