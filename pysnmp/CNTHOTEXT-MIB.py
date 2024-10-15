# SNMP MIB module (CNTHOTEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CNTHOTEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:03 2024
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

(cnthotExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "cnthotExt")

(apCntName,
 apCntOwner) = mibBuilder.importSymbols(
    "CNTEXT-MIB",
    "apCntName",
    "apCntOwner")

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

apCnthotExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 35, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApCnthotTable_Object = MibTable
apCnthotTable = _ApCnthotTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 35, 2)
)
if mibBuilder.loadTexts:
    apCnthotTable.setStatus("current")
_ApCnthotEntry_Object = MibTableRow
apCnthotEntry = _ApCnthotEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 35, 2, 1)
)
apCnthotEntry.setIndexNames(
    (0, "CNTEXT-MIB", "apCntOwner"),
    (0, "CNTEXT-MIB", "apCntName"),
    (0, "CNTHOTEXT-MIB", "apCnthotIndex"),
)
if mibBuilder.loadTexts:
    apCnthotEntry.setStatus("current")
_ApCnthotIndex_Type = Integer32
_ApCnthotIndex_Object = MibTableColumn
apCnthotIndex = _ApCnthotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 35, 2, 1, 1),
    _ApCnthotIndex_Type()
)
apCnthotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCnthotIndex.setStatus("current")
_ApCnthotRate_Type = Integer32
_ApCnthotRate_Object = MibTableColumn
apCnthotRate = _ApCnthotRate_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 35, 2, 1, 2),
    _ApCnthotRate_Type()
)
apCnthotRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCnthotRate.setStatus("current")


class _ApCnthotUri_Type(DisplayString):
    """Custom type apCnthotUri based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApCnthotUri_Type.__name__ = "DisplayString"
_ApCnthotUri_Object = MibTableColumn
apCnthotUri = _ApCnthotUri_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 35, 2, 1, 3),
    _ApCnthotUri_Type()
)
apCnthotUri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCnthotUri.setStatus("current")
_ApCnthotSize_Type = Integer32
_ApCnthotSize_Object = MibTableColumn
apCnthotSize = _ApCnthotSize_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 35, 2, 1, 4),
    _ApCnthotSize_Type()
)
apCnthotSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCnthotSize.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CNTHOTEXT-MIB",
    **{"apCnthotExtMib": apCnthotExtMib,
       "apCnthotTable": apCnthotTable,
       "apCnthotEntry": apCnthotEntry,
       "apCnthotIndex": apCnthotIndex,
       "apCnthotRate": apCnthotRate,
       "apCnthotUri": apCnthotUri,
       "apCnthotSize": apCnthotSize}
)
