# SNMP MIB module (PDN-DS1CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-DS1CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:32 2024
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

(pdn_interfaces,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-interfaces")

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

_Ent_ds1_ObjectIdentity = ObjectIdentity
ent_ds1 = _Ent_ds1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5)
)
_DevDS1Test_ObjectIdentity = ObjectIdentity
devDS1Test = _DevDS1Test_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 1)
)
_DevDS1TestTable_Object = MibTable
devDS1TestTable = _DevDS1TestTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 1, 1)
)
if mibBuilder.loadTexts:
    devDS1TestTable.setStatus("mandatory")
_DevDS1TestEntry_Object = MibTableRow
devDS1TestEntry = _DevDS1TestEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 1, 1, 1)
)
devDS1TestEntry.setIndexNames(
    (0, "PDN-DS1CONFIG-MIB", "devDS1TestIfIndex"),
    (0, "PDN-DS1CONFIG-MIB", "devDS1TestType"),
)
if mibBuilder.loadTexts:
    devDS1TestEntry.setStatus("mandatory")
_DevDS1TestIfIndex_Type = Integer32
_DevDS1TestIfIndex_Object = MibTableColumn
devDS1TestIfIndex = _DevDS1TestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 1, 1, 1, 1),
    _DevDS1TestIfIndex_Type()
)
devDS1TestIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDS1TestIfIndex.setStatus("mandatory")


class _DevDS1TestType_Type(Integer32):
    """Custom type devDS1TestType based on Integer32"""
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
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("llb", 3),
          ("llbdn", 2),
          ("llbup", 1),
          ("mon11", 23),
          ("mon1in8", 20),
          ("mon2047", 24),
          ("mon2E11", 31),
          ("mon2E15", 25),
          ("mon2E20", 26),
          ("mon2E7", 29),
          ("mon3in24", 21),
          ("mon63", 22),
          ("monOnes", 19),
          ("monQRSS", 17),
          ("monUserDefined", 27),
          ("monZeros", 18),
          ("plb", 4),
          ("rlb", 5),
          ("send1in8", 9),
          ("send2047", 13),
          ("send2E11", 30),
          ("send2E15", 14),
          ("send2E20", 15),
          ("send2E7", 28),
          ("send3in24", 10),
          ("send511", 12),
          ("send63", 11),
          ("sendOnes", 8),
          ("sendQRSS", 6),
          ("sendUserDefined", 16),
          ("sendZeros", 7))
    )


_DevDS1TestType_Type.__name__ = "Integer32"
_DevDS1TestType_Object = MibTableColumn
devDS1TestType = _DevDS1TestType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 1, 1, 1, 2),
    _DevDS1TestType_Type()
)
devDS1TestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDS1TestType.setStatus("mandatory")


class _DevDS1TestControl_Type(Integer32):
    """Custom type devDS1TestControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("running", 2))
    )


_DevDS1TestControl_Type.__name__ = "Integer32"
_DevDS1TestControl_Object = MibTableColumn
devDS1TestControl = _DevDS1TestControl_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 1, 1, 1, 3),
    _DevDS1TestControl_Type()
)
devDS1TestControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devDS1TestControl.setStatus("mandatory")


class _DevDS1TestArgument_Type(DisplayString):
    """Custom type devDS1TestArgument based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DevDS1TestArgument_Type.__name__ = "DisplayString"
_DevDS1TestArgument_Object = MibTableColumn
devDS1TestArgument = _DevDS1TestArgument_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 1, 1, 1, 4),
    _DevDS1TestArgument_Type()
)
devDS1TestArgument.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devDS1TestArgument.setStatus("mandatory")
_DevDS1MonResultTable_Object = MibTable
devDS1MonResultTable = _DevDS1MonResultTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 1, 2)
)
if mibBuilder.loadTexts:
    devDS1MonResultTable.setStatus("mandatory")
_DevDS1MonResultEntry_Object = MibTableRow
devDS1MonResultEntry = _DevDS1MonResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 1, 2, 1)
)
devDS1MonResultEntry.setIndexNames(
    (0, "PDN-DS1CONFIG-MIB", "devDS1MonResultIfIndex"),
    (0, "PDN-DS1CONFIG-MIB", "devDS1MonResultTestType"),
)
if mibBuilder.loadTexts:
    devDS1MonResultEntry.setStatus("mandatory")
_DevDS1MonResultIfIndex_Type = Integer32
_DevDS1MonResultIfIndex_Object = MibTableColumn
devDS1MonResultIfIndex = _DevDS1MonResultIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 1, 2, 1, 1),
    _DevDS1MonResultIfIndex_Type()
)
devDS1MonResultIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDS1MonResultIfIndex.setStatus("mandatory")


class _DevDS1MonResultTestType_Type(Integer32):
    """Custom type devDS1MonResultTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(17,
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
              29,
              31)
        )
    )
    namedValues = NamedValues(
        *(("mon11", 23),
          ("mon1in8", 20),
          ("mon2047", 24),
          ("mon2E11", 31),
          ("mon2E15", 25),
          ("mon2E20", 26),
          ("mon2E7", 29),
          ("mon3in24", 21),
          ("mon63", 22),
          ("monOnes", 19),
          ("monQRSS", 17),
          ("monUserDefined", 27),
          ("monZeros", 18))
    )


_DevDS1MonResultTestType_Type.__name__ = "Integer32"
_DevDS1MonResultTestType_Object = MibTableColumn
devDS1MonResultTestType = _DevDS1MonResultTestType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 1, 2, 1, 2),
    _DevDS1MonResultTestType_Type()
)
devDS1MonResultTestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDS1MonResultTestType.setStatus("mandatory")


class _DevDS1MonResultCode_Type(Integer32):
    """Custom type devDS1MonResultCode based on Integer32"""
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
        *(("inSyncNoBitErrors", 2),
          ("inSyncWithBitErrors", 3),
          ("none", 1),
          ("notInSync", 4))
    )


_DevDS1MonResultCode_Type.__name__ = "Integer32"
_DevDS1MonResultCode_Object = MibTableColumn
devDS1MonResultCode = _DevDS1MonResultCode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 1, 2, 1, 3),
    _DevDS1MonResultCode_Type()
)
devDS1MonResultCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDS1MonResultCode.setStatus("mandatory")
_DevDS1MonResultErrorCount_Type = Gauge32
_DevDS1MonResultErrorCount_Object = MibTableColumn
devDS1MonResultErrorCount = _DevDS1MonResultErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 1, 2, 1, 4),
    _DevDS1MonResultErrorCount_Type()
)
devDS1MonResultErrorCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devDS1MonResultErrorCount.setStatus("mandatory")
_DevDS1SendControlTable_Object = MibTable
devDS1SendControlTable = _DevDS1SendControlTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 1, 3)
)
if mibBuilder.loadTexts:
    devDS1SendControlTable.setStatus("mandatory")
_DevDS1SendControlEntry_Object = MibTableRow
devDS1SendControlEntry = _DevDS1SendControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 1, 3, 1)
)
devDS1SendControlEntry.setIndexNames(
    (0, "PDN-DS1CONFIG-MIB", "devDS1SendControlIfIndex"),
)
if mibBuilder.loadTexts:
    devDS1SendControlEntry.setStatus("mandatory")
_DevDS1SendControlIfIndex_Type = Integer32
_DevDS1SendControlIfIndex_Object = MibTableColumn
devDS1SendControlIfIndex = _DevDS1SendControlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 1, 3, 1, 1),
    _DevDS1SendControlIfIndex_Type()
)
devDS1SendControlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDS1SendControlIfIndex.setStatus("mandatory")


class _DevDS1SendControlInjectErr_Type(Integer32):
    """Custom type devDS1SendControlInjectErr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inject", 2),
          ("noOp", 1))
    )


_DevDS1SendControlInjectErr_Type.__name__ = "Integer32"
_DevDS1SendControlInjectErr_Object = MibTableColumn
devDS1SendControlInjectErr = _DevDS1SendControlInjectErr_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 1, 3, 1, 2),
    _DevDS1SendControlInjectErr_Type()
)
devDS1SendControlInjectErr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devDS1SendControlInjectErr.setStatus("mandatory")
_DevDS1SendControlErrorCount_Type = Gauge32
_DevDS1SendControlErrorCount_Object = MibTableColumn
devDS1SendControlErrorCount = _DevDS1SendControlErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 1, 3, 1, 3),
    _DevDS1SendControlErrorCount_Type()
)
devDS1SendControlErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDS1SendControlErrorCount.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-DS1CONFIG-MIB",
    **{"ent-ds1": ent_ds1,
       "devDS1Test": devDS1Test,
       "devDS1TestTable": devDS1TestTable,
       "devDS1TestEntry": devDS1TestEntry,
       "devDS1TestIfIndex": devDS1TestIfIndex,
       "devDS1TestType": devDS1TestType,
       "devDS1TestControl": devDS1TestControl,
       "devDS1TestArgument": devDS1TestArgument,
       "devDS1MonResultTable": devDS1MonResultTable,
       "devDS1MonResultEntry": devDS1MonResultEntry,
       "devDS1MonResultIfIndex": devDS1MonResultIfIndex,
       "devDS1MonResultTestType": devDS1MonResultTestType,
       "devDS1MonResultCode": devDS1MonResultCode,
       "devDS1MonResultErrorCount": devDS1MonResultErrorCount,
       "devDS1SendControlTable": devDS1SendControlTable,
       "devDS1SendControlEntry": devDS1SendControlEntry,
       "devDS1SendControlIfIndex": devDS1SendControlIfIndex,
       "devDS1SendControlInjectErr": devDS1SendControlInjectErr,
       "devDS1SendControlErrorCount": devDS1SendControlErrorCount}
)
