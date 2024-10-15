# SNMP MIB module (ASCEND-MISC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MISC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:37 2024
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

(miscGroup,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "miscGroup")

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

_MiscGroupFRTable_Object = MibTable
miscGroupFRTable = _MiscGroupFRTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 20, 1)
)
if mibBuilder.loadTexts:
    miscGroupFRTable.setStatus("mandatory")
_MiscGroupFREntry_Object = MibTableRow
miscGroupFREntry = _MiscGroupFREntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 20, 1, 1)
)
miscGroupFREntry.setIndexNames(
    (0, "ASCEND-MISC-MIB", "miscGroupFRLMIIndex"),
)
if mibBuilder.loadTexts:
    miscGroupFREntry.setStatus("mandatory")
_MiscGroupFRLMIIndex_Type = Integer32
_MiscGroupFRLMIIndex_Object = MibTableColumn
miscGroupFRLMIIndex = _MiscGroupFRLMIIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 20, 1, 1, 1),
    _MiscGroupFRLMIIndex_Type()
)
miscGroupFRLMIIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscGroupFRLMIIndex.setStatus("mandatory")


class _MiscGroupFRLMIDlci_Type(Integer32):
    """Custom type miscGroupFRLMIDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dlci-0", 1),
          ("dlci-1023", 2))
    )


_MiscGroupFRLMIDlci_Type.__name__ = "Integer32"
_MiscGroupFRLMIDlci_Object = MibTableColumn
miscGroupFRLMIDlci = _MiscGroupFRLMIDlci_Object(
    (1, 3, 6, 1, 4, 1, 529, 20, 1, 1, 2),
    _MiscGroupFRLMIDlci_Type()
)
miscGroupFRLMIDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscGroupFRLMIDlci.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MISC-MIB",
    **{"miscGroupFRTable": miscGroupFRTable,
       "miscGroupFREntry": miscGroupFREntry,
       "miscGroupFRLMIIndex": miscGroupFRLMIIndex,
       "miscGroupFRLMIDlci": miscGroupFRLMIDlci}
)
