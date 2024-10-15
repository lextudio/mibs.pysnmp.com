# SNMP MIB module (CXUTST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXUTST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:56 2024
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

(cxUTst,) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "cxUTst")

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

_UtstTable_Object = MibTable
utstTable = _UtstTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 40, 10)
)
if mibBuilder.loadTexts:
    utstTable.setStatus("mandatory")
_UtstEntry_Object = MibTableRow
utstEntry = _UtstEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 40, 10, 1)
)
utstEntry.setIndexNames(
    (0, "CXUTST-MIB", "utstSlotNumberIndex"),
)
if mibBuilder.loadTexts:
    utstEntry.setStatus("mandatory")


class _UtstSlotNumberIndex_Type(Integer32):
    """Custom type utstSlotNumberIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_UtstSlotNumberIndex_Type.__name__ = "Integer32"
_UtstSlotNumberIndex_Object = MibTableColumn
utstSlotNumberIndex = _UtstSlotNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 40, 10, 1, 1),
    _UtstSlotNumberIndex_Type()
)
utstSlotNumberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utstSlotNumberIndex.setStatus("mandatory")


class _UtstIoRegTest_Type(Integer32):
    """Custom type utstIoRegTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("passed", 2))
    )


_UtstIoRegTest_Type.__name__ = "Integer32"
_UtstIoRegTest_Object = MibTableColumn
utstIoRegTest = _UtstIoRegTest_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 40, 10, 1, 20),
    _UtstIoRegTest_Type()
)
utstIoRegTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utstIoRegTest.setStatus("mandatory")


class _UtstIoLedsTest_Type(Integer32):
    """Custom type utstIoLedsTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initializationFailed", 1),
          ("initializationPassed", 2))
    )


_UtstIoLedsTest_Type.__name__ = "Integer32"
_UtstIoLedsTest_Object = MibTableColumn
utstIoLedsTest = _UtstIoLedsTest_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 40, 10, 1, 21),
    _UtstIoLedsTest_Type()
)
utstIoLedsTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utstIoLedsTest.setStatus("mandatory")


class _UtstImpRegTest_Type(Integer32):
    """Custom type utstImpRegTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("initializationFailed", 1),
          ("passed", 3))
    )


_UtstImpRegTest_Type.__name__ = "Integer32"
_UtstImpRegTest_Object = MibTableColumn
utstImpRegTest = _UtstImpRegTest_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 40, 10, 1, 22),
    _UtstImpRegTest_Type()
)
utstImpRegTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utstImpRegTest.setStatus("mandatory")


class _UtstImpComTestPollResult_Type(Integer32):
    """Custom type utstImpComTestPollResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("initializationFailed", 1),
          ("passed", 3))
    )


_UtstImpComTestPollResult_Type.__name__ = "Integer32"
_UtstImpComTestPollResult_Object = MibTableColumn
utstImpComTestPollResult = _UtstImpComTestPollResult_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 40, 10, 1, 23),
    _UtstImpComTestPollResult_Type()
)
utstImpComTestPollResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utstImpComTestPollResult.setStatus("mandatory")


class _UtstUifRegTest_Type(Integer32):
    """Custom type utstUifRegTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("initializationFailed", 1),
          ("passed", 3))
    )


_UtstUifRegTest_Type.__name__ = "Integer32"
_UtstUifRegTest_Object = MibTableColumn
utstUifRegTest = _UtstUifRegTest_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 40, 10, 1, 24),
    _UtstUifRegTest_Type()
)
utstUifRegTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utstUifRegTest.setStatus("mandatory")


class _UtstUifComTestPollResult_Type(Integer32):
    """Custom type utstUifComTestPollResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("initializationFailed", 1),
          ("passed", 3))
    )


_UtstUifComTestPollResult_Type.__name__ = "Integer32"
_UtstUifComTestPollResult_Object = MibTableColumn
utstUifComTestPollResult = _UtstUifComTestPollResult_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 40, 10, 1, 25),
    _UtstUifComTestPollResult_Type()
)
utstUifComTestPollResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    utstUifComTestPollResult.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXUTST-MIB",
    **{"utstTable": utstTable,
       "utstEntry": utstEntry,
       "utstSlotNumberIndex": utstSlotNumberIndex,
       "utstIoRegTest": utstIoRegTest,
       "utstIoLedsTest": utstIoLedsTest,
       "utstImpRegTest": utstImpRegTest,
       "utstImpComTestPollResult": utstImpComTestPollResult,
       "utstUifRegTest": utstUifRegTest,
       "utstUifComTestPollResult": utstUifComTestPollResult}
)
