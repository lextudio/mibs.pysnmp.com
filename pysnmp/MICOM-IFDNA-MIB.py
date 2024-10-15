# SNMP MIB module (MICOM-IFDNA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MICOM-IFDNA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:42 2024
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

(micom_oscar,) = mibBuilder.importSymbols(
    "MICOM-OSCAR-MIB",
    "micom-oscar")

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

_Micom_ifdna_ObjectIdentity = ObjectIdentity
micom_ifdna = _Micom_ifdna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 18)
)
_IfDna_ObjectIdentity = ObjectIdentity
ifDna = _IfDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 18, 1)
)
_McmIfDnaTable_Object = MibTable
mcmIfDnaTable = _McmIfDnaTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 18, 1, 1)
)
if mibBuilder.loadTexts:
    mcmIfDnaTable.setStatus("mandatory")
_McmIfDnaEntry_Object = MibTableRow
mcmIfDnaEntry = _McmIfDnaEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 18, 1, 1, 1)
)
mcmIfDnaEntry.setIndexNames(
    (0, "MICOM-IFDNA-MIB", "mcmIfDnaIfIndex"),
    (0, "MICOM-IFDNA-MIB", "mcmIfDnaType"),
)
if mibBuilder.loadTexts:
    mcmIfDnaEntry.setStatus("mandatory")


class _McmIfDnaIfIndex_Type(Integer32):
    """Custom type mcmIfDnaIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmIfDnaIfIndex_Type.__name__ = "Integer32"
_McmIfDnaIfIndex_Object = MibTableColumn
mcmIfDnaIfIndex = _McmIfDnaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 18, 1, 1, 1, 1),
    _McmIfDnaIfIndex_Type()
)
mcmIfDnaIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIfDnaIfIndex.setStatus("mandatory")


class _McmIfDnaType_Type(Integer32):
    """Custom type mcmIfDnaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("learnt", 2),
          ("provisioned", 1))
    )


_McmIfDnaType_Type.__name__ = "Integer32"
_McmIfDnaType_Object = MibTableColumn
mcmIfDnaType = _McmIfDnaType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 18, 1, 1, 1, 2),
    _McmIfDnaType_Type()
)
mcmIfDnaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmIfDnaType.setStatus("mandatory")


class _McmIfDNADigits_Type(DisplayString):
    """Custom type mcmIfDNADigits based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 34),
    )


_McmIfDNADigits_Type.__name__ = "DisplayString"
_McmIfDNADigits_Object = MibTableColumn
mcmIfDNADigits = _McmIfDNADigits_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 18, 1, 1, 1, 3),
    _McmIfDNADigits_Type()
)
mcmIfDNADigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmIfDNADigits.setStatus("mandatory")


class _McmIfDnaStatus_Type(Integer32):
    """Custom type mcmIfDnaStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("invalid", 3),
          ("valid", 1))
    )


_McmIfDnaStatus_Type.__name__ = "Integer32"
_McmIfDnaStatus_Object = MibTableColumn
mcmIfDnaStatus = _McmIfDnaStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 18, 1, 1, 1, 4),
    _McmIfDnaStatus_Type()
)
mcmIfDnaStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmIfDnaStatus.setStatus("mandatory")
_IfNvDna_ObjectIdentity = ObjectIdentity
ifNvDna = _IfNvDna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 18, 2)
)
_NvmIfDnaTable_Object = MibTable
nvmIfDnaTable = _NvmIfDnaTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 18, 2, 1)
)
if mibBuilder.loadTexts:
    nvmIfDnaTable.setStatus("mandatory")
_NvmIfDnaEntry_Object = MibTableRow
nvmIfDnaEntry = _NvmIfDnaEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 18, 2, 1, 1)
)
nvmIfDnaEntry.setIndexNames(
    (0, "MICOM-IFDNA-MIB", "nvmIfDnaIfIndex"),
    (0, "MICOM-IFDNA-MIB", "nvmIfDnaType"),
)
if mibBuilder.loadTexts:
    nvmIfDnaEntry.setStatus("mandatory")


class _NvmIfDnaIfIndex_Type(Integer32):
    """Custom type nvmIfDnaIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmIfDnaIfIndex_Type.__name__ = "Integer32"
_NvmIfDnaIfIndex_Object = MibTableColumn
nvmIfDnaIfIndex = _NvmIfDnaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 18, 2, 1, 1, 1),
    _NvmIfDnaIfIndex_Type()
)
nvmIfDnaIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmIfDnaIfIndex.setStatus("mandatory")


class _NvmIfDnaType_Type(Integer32):
    """Custom type nvmIfDnaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("learnt", 2),
          ("provisioned", 1))
    )


_NvmIfDnaType_Type.__name__ = "Integer32"
_NvmIfDnaType_Object = MibTableColumn
nvmIfDnaType = _NvmIfDnaType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 18, 2, 1, 1, 2),
    _NvmIfDnaType_Type()
)
nvmIfDnaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmIfDnaType.setStatus("mandatory")


class _NvmIfDNADigits_Type(DisplayString):
    """Custom type nvmIfDNADigits based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 34),
    )


_NvmIfDNADigits_Type.__name__ = "DisplayString"
_NvmIfDNADigits_Object = MibTableColumn
nvmIfDNADigits = _NvmIfDNADigits_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 18, 2, 1, 1, 3),
    _NvmIfDNADigits_Type()
)
nvmIfDNADigits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmIfDNADigits.setStatus("mandatory")


class _NvmIfDnaStatus_Type(Integer32):
    """Custom type nvmIfDnaStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("invalid", 3),
          ("valid", 1))
    )


_NvmIfDnaStatus_Type.__name__ = "Integer32"
_NvmIfDnaStatus_Object = MibTableColumn
nvmIfDnaStatus = _NvmIfDnaStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 18, 2, 1, 1, 4),
    _NvmIfDnaStatus_Type()
)
nvmIfDnaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmIfDnaStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MICOM-IFDNA-MIB",
    **{"micom-ifdna": micom_ifdna,
       "ifDna": ifDna,
       "mcmIfDnaTable": mcmIfDnaTable,
       "mcmIfDnaEntry": mcmIfDnaEntry,
       "mcmIfDnaIfIndex": mcmIfDnaIfIndex,
       "mcmIfDnaType": mcmIfDnaType,
       "mcmIfDNADigits": mcmIfDNADigits,
       "mcmIfDnaStatus": mcmIfDnaStatus,
       "ifNvDna": ifNvDna,
       "nvmIfDnaTable": nvmIfDnaTable,
       "nvmIfDnaEntry": nvmIfDnaEntry,
       "nvmIfDnaIfIndex": nvmIfDnaIfIndex,
       "nvmIfDnaType": nvmIfDnaType,
       "nvmIfDNADigits": nvmIfDNADigits,
       "nvmIfDnaStatus": nvmIfDnaStatus}
)
