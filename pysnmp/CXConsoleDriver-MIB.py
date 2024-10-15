# SNMP MIB module (CXConsoleDriver-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXConsoleDriver-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:16 2024
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

(cxConsoleDriver,) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "cxConsoleDriver")

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



class _CxCdBaudRate_Type(Integer32):
    """Custom type cxCdBaudRate based on Integer32"""
    defaultValue = 9600


_CxCdBaudRate_Object = MibScalar
cxCdBaudRate = _CxCdBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 6, 1),
    _CxCdBaudRate_Type()
)
cxCdBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCdBaudRate.setStatus("mandatory")


class _CxCdCharSize_Type(Integer32):
    """Custom type cxCdCharSize based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 8),
    )


_CxCdCharSize_Type.__name__ = "Integer32"
_CxCdCharSize_Object = MibScalar
cxCdCharSize = _CxCdCharSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 6, 2),
    _CxCdCharSize_Type()
)
cxCdCharSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCdCharSize.setStatus("mandatory")


class _CxCdParity_Type(Integer32):
    """Custom type cxCdParity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("evenParity", 2),
          ("noParity", 1),
          ("oddParity", 3))
    )


_CxCdParity_Type.__name__ = "Integer32"
_CxCdParity_Object = MibScalar
cxCdParity = _CxCdParity_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 6, 3),
    _CxCdParity_Type()
)
cxCdParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCdParity.setStatus("mandatory")


class _CxCdStopBit_Type(Integer32):
    """Custom type cxCdStopBit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CxCdStopBit_Type.__name__ = "Integer32"
_CxCdStopBit_Object = MibScalar
cxCdStopBit = _CxCdStopBit_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 6, 4),
    _CxCdStopBit_Type()
)
cxCdStopBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCdStopBit.setStatus("mandatory")


class _CxCdProtocol_Type(Integer32):
    """Custom type cxCdProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localConsole", 1),
          ("ppp", 2))
    )


_CxCdProtocol_Type.__name__ = "Integer32"
_CxCdProtocol_Object = MibScalar
cxCdProtocol = _CxCdProtocol_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 6, 5),
    _CxCdProtocol_Type()
)
cxCdProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxCdProtocol.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXConsoleDriver-MIB",
    **{"cxCdBaudRate": cxCdBaudRate,
       "cxCdCharSize": cxCdCharSize,
       "cxCdParity": cxCdParity,
       "cxCdStopBit": cxCdStopBit,
       "cxCdProtocol": cxCdProtocol}
)
