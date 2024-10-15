# SNMP MIB module (GENERICOBJECT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GENERICOBJECT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:00 2024
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

(cardGeneric,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "cardGeneric")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GenericObjects_ObjectIdentity = ObjectIdentity
genericObjects = _GenericObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 8)
)
_GenericLineNum_Type = Integer32
_GenericLineNum_Object = MibScalar
genericLineNum = _GenericLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 8, 1),
    _GenericLineNum_Type()
)
genericLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericLineNum.setStatus("mandatory")


class _GenericLineType_Type(Integer32):
    """Custom type genericLineType based on Integer32"""
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
              51,
              52,
              53,
              54,
              55,
              56,
              101,
              102,
              151,
              152,
              153,
              154)
        )
    )
    namedValues = NamedValues(
        *(("dsx1D4", 2),
          ("dsx1E1", 3),
          ("dsx1E1CRC", 4),
          ("dsx1E1CRC-MF", 6),
          ("dsx1E1MF", 5),
          ("dsx1E1clearchannel", 7),
          ("dsx1ESF", 1),
          ("dsx3CbitParity", 51),
          ("dsx3Unframed", 55),
          ("dsx3g751", 54),
          ("dsx3g832-g804", 52),
          ("dsx3m13mode", 53),
          ("e3Unframed", 56),
          ("sonetStm1", 152),
          ("sonetStm4", 154),
          ("sonetSts12c", 153),
          ("sonetSts3c", 151),
          ("x21dce", 102),
          ("x21dte", 101))
    )


_GenericLineType_Type.__name__ = "Integer32"
_GenericLineType_Object = MibScalar
genericLineType = _GenericLineType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 8, 2),
    _GenericLineType_Type()
)
genericLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericLineType.setStatus("mandatory")


class _GenericTimeStamp_Type(DisplayString):
    """Custom type genericTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_GenericTimeStamp_Type.__name__ = "DisplayString"
_GenericTimeStamp_Object = MibScalar
genericTimeStamp = _GenericTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 2, 8, 3),
    _GenericTimeStamp_Type()
)
genericTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericTimeStamp.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GENERICOBJECT-MIB",
    **{"genericObjects": genericObjects,
       "genericLineNum": genericLineNum,
       "genericLineType": genericLineType,
       "genericTimeStamp": genericTimeStamp}
)
