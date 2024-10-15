# SNMP MIB module (NBS-FEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NBS-FEC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:49 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(nbs,) = mibBuilder.importSymbols(
    "NBS-MIB",
    "nbs")

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

nbsFecMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 232)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NbsFecCode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("gfec", 3),
          ("hgfec7", 7),
          ("noFec", 1),
          ("notSupported", 0),
          ("sdfec0", 8),
          ("sdfec1", 9),
          ("sdfec2", 10),
          ("sdfec3", 11),
          ("strong1dot4", 12),
          ("strong1dot7", 13),
          ("ufec10", 5),
          ("ufec25", 6),
          ("ufec7", 4),
          ("zero", 2))
    )



# MIB Managed Objects in the order of their OIDs

_NbsFecCfgGrp_ObjectIdentity = ObjectIdentity
nbsFecCfgGrp = _NbsFecCfgGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 232, 1)
)
if mibBuilder.loadTexts:
    nbsFecCfgGrp.setStatus("current")
_NbsFecCfgTable_Object = MibTable
nbsFecCfgTable = _NbsFecCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 232, 1, 1)
)
if mibBuilder.loadTexts:
    nbsFecCfgTable.setStatus("current")
_NbsFecCfgEntry_Object = MibTableRow
nbsFecCfgEntry = _NbsFecCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 232, 1, 1, 1)
)
nbsFecCfgEntry.setIndexNames(
    (0, "NBS-FEC-MIB", "nbsFecCfgIfIndex"),
)
if mibBuilder.loadTexts:
    nbsFecCfgEntry.setStatus("current")
_NbsFecCfgIfIndex_Type = InterfaceIndex
_NbsFecCfgIfIndex_Object = MibTableColumn
nbsFecCfgIfIndex = _NbsFecCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 232, 1, 1, 1, 1),
    _NbsFecCfgIfIndex_Type()
)
nbsFecCfgIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsFecCfgIfIndex.setStatus("current")


class _NbsFecCfgCodeCaps_Type(OctetString):
    """Custom type nbsFecCfgCodeCaps based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_NbsFecCfgCodeCaps_Type.__name__ = "OctetString"
_NbsFecCfgCodeCaps_Object = MibTableColumn
nbsFecCfgCodeCaps = _NbsFecCfgCodeCaps_Object(
    (1, 3, 6, 1, 4, 1, 629, 232, 1, 1, 1, 2),
    _NbsFecCfgCodeCaps_Type()
)
nbsFecCfgCodeCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecCfgCodeCaps.setStatus("current")
_NbsFecCfgCodeAdmin_Type = NbsFecCode
_NbsFecCfgCodeAdmin_Object = MibTableColumn
nbsFecCfgCodeAdmin = _NbsFecCfgCodeAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 232, 1, 1, 1, 3),
    _NbsFecCfgCodeAdmin_Type()
)
nbsFecCfgCodeAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsFecCfgCodeAdmin.setStatus("current")
_NbsFecCfgCodeOper_Type = NbsFecCode
_NbsFecCfgCodeOper_Object = MibTableColumn
nbsFecCfgCodeOper = _NbsFecCfgCodeOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 232, 1, 1, 1, 4),
    _NbsFecCfgCodeOper_Type()
)
nbsFecCfgCodeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecCfgCodeOper.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-FEC-MIB",
    **{"NbsFecCode": NbsFecCode,
       "nbsFecMib": nbsFecMib,
       "nbsFecCfgGrp": nbsFecCfgGrp,
       "nbsFecCfgTable": nbsFecCfgTable,
       "nbsFecCfgEntry": nbsFecCfgEntry,
       "nbsFecCfgIfIndex": nbsFecCfgIfIndex,
       "nbsFecCfgCodeCaps": nbsFecCfgCodeCaps,
       "nbsFecCfgCodeAdmin": nbsFecCfgCodeAdmin,
       "nbsFecCfgCodeOper": nbsFecCfgCodeOper}
)
