# SNMP MIB module (CTRON-IF-REMAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-IF-REMAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:55 2024
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

(ctIFRemap,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctIFRemap")

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

_CtIfRemapConfig_ObjectIdentity = ObjectIdentity
ctIfRemapConfig = _CtIfRemapConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 13, 1)
)
_CtIFRemapTable_Object = MibTable
ctIFRemapTable = _CtIFRemapTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 13, 1, 1)
)
if mibBuilder.loadTexts:
    ctIFRemapTable.setStatus("mandatory")
_CtIFRemapEntry_Object = MibTableRow
ctIFRemapEntry = _CtIFRemapEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 13, 1, 1, 1)
)
ctIFRemapEntry.setIndexNames(
    (0, "CTRON-IF-REMAP-MIB", "ctIfRemapSourceIf"),
    (0, "CTRON-IF-REMAP-MIB", "ctIfRemapDestIf"),
)
if mibBuilder.loadTexts:
    ctIFRemapEntry.setStatus("mandatory")
_CtIfRemapSourceIf_Type = Integer32
_CtIfRemapSourceIf_Object = MibTableColumn
ctIfRemapSourceIf = _CtIfRemapSourceIf_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 13, 1, 1, 1, 1),
    _CtIfRemapSourceIf_Type()
)
ctIfRemapSourceIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIfRemapSourceIf.setStatus("mandatory")
_CtIfRemapDestIf_Type = Integer32
_CtIfRemapDestIf_Object = MibTableColumn
ctIfRemapDestIf = _CtIfRemapDestIf_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 13, 1, 1, 1, 2),
    _CtIfRemapDestIf_Type()
)
ctIfRemapDestIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIfRemapDestIf.setStatus("mandatory")


class _CtIfRemapStatus_Type(Integer32):
    """Custom type ctIfRemapStatus based on Integer32"""
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


_CtIfRemapStatus_Type.__name__ = "Integer32"
_CtIfRemapStatus_Object = MibTableColumn
ctIfRemapStatus = _CtIfRemapStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 13, 1, 1, 1, 3),
    _CtIfRemapStatus_Type()
)
ctIfRemapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctIfRemapStatus.setStatus("mandatory")
_CtIfRemapTableNumberEntries_Type = Integer32
_CtIfRemapTableNumberEntries_Object = MibScalar
ctIfRemapTableNumberEntries = _CtIfRemapTableNumberEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 13, 2),
    _CtIfRemapTableNumberEntries_Type()
)
ctIfRemapTableNumberEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIfRemapTableNumberEntries.setStatus("mandatory")
_CtIfRemapTableMaxNumberEntries_Type = Integer32
_CtIfRemapTableMaxNumberEntries_Object = MibScalar
ctIfRemapTableMaxNumberEntries = _CtIfRemapTableMaxNumberEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 13, 3),
    _CtIfRemapTableMaxNumberEntries_Type()
)
ctIfRemapTableMaxNumberEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIfRemapTableMaxNumberEntries.setStatus("mandatory")


class _CtIfRemapPhysicalErrorsEnable_Type(Integer32):
    """Custom type ctIfRemapPhysicalErrorsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("unsupported", 3))
    )


_CtIfRemapPhysicalErrorsEnable_Type.__name__ = "Integer32"
_CtIfRemapPhysicalErrorsEnable_Object = MibScalar
ctIfRemapPhysicalErrorsEnable = _CtIfRemapPhysicalErrorsEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 13, 4),
    _CtIfRemapPhysicalErrorsEnable_Type()
)
ctIfRemapPhysicalErrorsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctIfRemapPhysicalErrorsEnable.setStatus("mandatory")


class _CtIfRemapTableEnable_Type(Integer32):
    """Custom type ctIfRemapTableEnable based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("unsupported", 3))
    )


_CtIfRemapTableEnable_Type.__name__ = "Integer32"
_CtIfRemapTableEnable_Object = MibScalar
ctIfRemapTableEnable = _CtIfRemapTableEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 13, 5),
    _CtIfRemapTableEnable_Type()
)
ctIfRemapTableEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctIfRemapTableEnable.setStatus("mandatory")


class _CtIfRemapTableStart_Type(Integer32):
    """Custom type ctIfRemapTableStart based on Integer32"""
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
        *(("start", 1),
          ("stop", 2),
          ("unsupported", 3))
    )


_CtIfRemapTableStart_Type.__name__ = "Integer32"
_CtIfRemapTableStart_Object = MibScalar
ctIfRemapTableStart = _CtIfRemapTableStart_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 13, 6),
    _CtIfRemapTableStart_Type()
)
ctIfRemapTableStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctIfRemapTableStart.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-IF-REMAP-MIB",
    **{"ctIfRemapConfig": ctIfRemapConfig,
       "ctIFRemapTable": ctIFRemapTable,
       "ctIFRemapEntry": ctIFRemapEntry,
       "ctIfRemapSourceIf": ctIfRemapSourceIf,
       "ctIfRemapDestIf": ctIfRemapDestIf,
       "ctIfRemapStatus": ctIfRemapStatus,
       "ctIfRemapTableNumberEntries": ctIfRemapTableNumberEntries,
       "ctIfRemapTableMaxNumberEntries": ctIfRemapTableMaxNumberEntries,
       "ctIfRemapPhysicalErrorsEnable": ctIfRemapPhysicalErrorsEnable,
       "ctIfRemapTableEnable": ctIfRemapTableEnable,
       "ctIfRemapTableStart": ctIfRemapTableStart}
)
