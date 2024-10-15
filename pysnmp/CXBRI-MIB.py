# SNMP MIB module (CXBRI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXBRI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:08 2024
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

(cxBri,) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "cxBri")

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

_BriTable_Object = MibTable
briTable = _BriTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 4, 10)
)
if mibBuilder.loadTexts:
    briTable.setStatus("mandatory")
_BriEntry_Object = MibTableRow
briEntry = _BriEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 4, 10, 1)
)
briEntry.setIndexNames(
    (0, "CXBRI-MIB", "briSlotNumberIndex"),
)
if mibBuilder.loadTexts:
    briEntry.setStatus("mandatory")


class _BriSlotNumberIndex_Type(Integer32):
    """Custom type briSlotNumberIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BriSlotNumberIndex_Type.__name__ = "Integer32"
_BriSlotNumberIndex_Object = MibTableColumn
briSlotNumberIndex = _BriSlotNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 4, 10, 1, 1),
    _BriSlotNumberIndex_Type()
)
briSlotNumberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    briSlotNumberIndex.setStatus("mandatory")


class _BriIoRegTest_Type(Integer32):
    """Custom type briIoRegTest based on Integer32"""
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


_BriIoRegTest_Type.__name__ = "Integer32"
_BriIoRegTest_Object = MibTableColumn
briIoRegTest = _BriIoRegTest_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 4, 10, 1, 20),
    _BriIoRegTest_Type()
)
briIoRegTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    briIoRegTest.setStatus("mandatory")


class _BriIoLedsTest_Type(Integer32):
    """Custom type briIoLedsTest based on Integer32"""
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


_BriIoLedsTest_Type.__name__ = "Integer32"
_BriIoLedsTest_Object = MibTableColumn
briIoLedsTest = _BriIoLedsTest_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 4, 10, 1, 21),
    _BriIoLedsTest_Type()
)
briIoLedsTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    briIoLedsTest.setStatus("mandatory")


class _BriImpRegTest_Type(Integer32):
    """Custom type briImpRegTest based on Integer32"""
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


_BriImpRegTest_Type.__name__ = "Integer32"
_BriImpRegTest_Object = MibTableColumn
briImpRegTest = _BriImpRegTest_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 4, 10, 1, 22),
    _BriImpRegTest_Type()
)
briImpRegTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    briImpRegTest.setStatus("mandatory")


class _BriImpComTestPollResult_Type(Integer32):
    """Custom type briImpComTestPollResult based on Integer32"""
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


_BriImpComTestPollResult_Type.__name__ = "Integer32"
_BriImpComTestPollResult_Object = MibTableColumn
briImpComTestPollResult = _BriImpComTestPollResult_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 4, 10, 1, 23),
    _BriImpComTestPollResult_Type()
)
briImpComTestPollResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    briImpComTestPollResult.setStatus("mandatory")


class _BriTxcvrRegTest_Type(Integer32):
    """Custom type briTxcvrRegTest based on Integer32"""
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


_BriTxcvrRegTest_Type.__name__ = "Integer32"
_BriTxcvrRegTest_Object = MibTableColumn
briTxcvrRegTest = _BriTxcvrRegTest_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 4, 10, 1, 24),
    _BriTxcvrRegTest_Type()
)
briTxcvrRegTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    briTxcvrRegTest.setStatus("mandatory")


class _BriTxcvrComTestPollResult_Type(Integer32):
    """Custom type briTxcvrComTestPollResult based on Integer32"""
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


_BriTxcvrComTestPollResult_Type.__name__ = "Integer32"
_BriTxcvrComTestPollResult_Object = MibTableColumn
briTxcvrComTestPollResult = _BriTxcvrComTestPollResult_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 4, 10, 1, 25),
    _BriTxcvrComTestPollResult_Type()
)
briTxcvrComTestPollResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    briTxcvrComTestPollResult.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXBRI-MIB",
    **{"briTable": briTable,
       "briEntry": briEntry,
       "briSlotNumberIndex": briSlotNumberIndex,
       "briIoRegTest": briIoRegTest,
       "briIoLedsTest": briIoLedsTest,
       "briImpRegTest": briImpRegTest,
       "briImpComTestPollResult": briImpComTestPollResult,
       "briTxcvrRegTest": briTxcvrRegTest,
       "briTxcvrComTestPollResult": briTxcvrComTestPollResult}
)
