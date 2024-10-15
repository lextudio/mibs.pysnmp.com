# SNMP MIB module (CISCO-DMN-DSG-BISS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DMN-DSG-BISS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:16 2024
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoDSGBISS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 38)
)
ciscoDSGBISS.setRevisions(
        ("2010-08-02 07:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _BissMode_Type(Integer32):
    """Custom type bissMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mode1", 1),
          ("modeE", 2))
    )


_BissMode_Type.__name__ = "Integer32"
_BissMode_Object = MibScalar
bissMode = _BissMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 38, 1),
    _BissMode_Type()
)
bissMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bissMode.setStatus("current")


class _BissMode1SessionWord_Type(DisplayString):
    """Custom type bissMode1SessionWord based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_BissMode1SessionWord_Type.__name__ = "DisplayString"
_BissMode1SessionWord_Object = MibScalar
bissMode1SessionWord = _BissMode1SessionWord_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 38, 2),
    _BissMode1SessionWord_Type()
)
bissMode1SessionWord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bissMode1SessionWord.setStatus("current")


class _BissModeESessionWord_Type(DisplayString):
    """Custom type bissModeESessionWord based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_BissModeESessionWord_Type.__name__ = "DisplayString"
_BissModeESessionWord_Object = MibScalar
bissModeESessionWord = _BissModeESessionWord_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 38, 3),
    _BissModeESessionWord_Type()
)
bissModeESessionWord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bissModeESessionWord.setStatus("current")


class _BissModeEInjectedId_Type(DisplayString):
    """Custom type bissModeEInjectedId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_BissModeEInjectedId_Type.__name__ = "DisplayString"
_BissModeEInjectedId_Object = MibScalar
bissModeEInjectedId = _BissModeEInjectedId_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 38, 4),
    _BissModeEInjectedId_Type()
)
bissModeEInjectedId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bissModeEInjectedId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-BISS-MIB",
    **{"ciscoDSGBISS": ciscoDSGBISS,
       "bissMode": bissMode,
       "bissMode1SessionWord": bissMode1SessionWord,
       "bissModeESessionWord": bissModeESessionWord,
       "bissModeEInjectedId": bissModeEInjectedId}
)
