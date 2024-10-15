# SNMP MIB module (CXPhysicalInterfaceManager-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXPhysicalInterfaceManager-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:45 2024
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

(cxPortManager,) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "cxPortManager")

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

_CxPhyIfTable_Object = MibTable
cxPhyIfTable = _CxPhyIfTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 16, 3)
)
if mibBuilder.loadTexts:
    cxPhyIfTable.setStatus("mandatory")
_CxPhyIfEntry_Object = MibTableRow
cxPhyIfEntry = _CxPhyIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 16, 3, 1)
)
cxPhyIfEntry.setIndexNames(
    (0, "CXPhysicalInterfaceManager-MIB", "cxPhyIfIndex"),
)
if mibBuilder.loadTexts:
    cxPhyIfEntry.setStatus("mandatory")
_CxPhyIfIndex_Type = Integer32
_CxPhyIfIndex_Object = MibTableColumn
cxPhyIfIndex = _CxPhyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 16, 3, 1, 1),
    _CxPhyIfIndex_Type()
)
cxPhyIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxPhyIfIndex.setStatus("mandatory")


class _CxPhyIfType_Type(Integer32):
    """Custom type cxPhyIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              8,
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
              28)
        )
    )
    namedValues = NamedValues(
        *(("atm-cell-io", 28),
          ("dds-56k", 10),
          ("dds-t1e1", 11),
          ("dvc", 25),
          ("elIO", 21),
          ("em-voice", 14),
          ("ethernet", 15),
          ("fast-ethernet", 27),
          ("fxo-voice", 13),
          ("fxs-voice", 12),
          ("hsIO", 18),
          ("lanIO", 20),
          ("multi-io", 26),
          ("others", 1),
          ("st-isdn-bri", 8),
          ("t1e1IO", 24),
          ("tlIO", 23),
          ("token-ring", 16),
          ("u-isdn-bri", 6),
          ("usIO", 19),
          ("v24", 2),
          ("v34", 5),
          ("v35", 3),
          ("v35-eu", 17),
          ("voxIO", 22),
          ("x21", 4))
    )


_CxPhyIfType_Type.__name__ = "Integer32"
_CxPhyIfType_Object = MibTableColumn
cxPhyIfType = _CxPhyIfType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 16, 3, 1, 2),
    _CxPhyIfType_Type()
)
cxPhyIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxPhyIfType.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXPhysicalInterfaceManager-MIB",
    **{"cxPhyIfTable": cxPhyIfTable,
       "cxPhyIfEntry": cxPhyIfEntry,
       "cxPhyIfIndex": cxPhyIfIndex,
       "cxPhyIfType": cxPhyIfType}
)
