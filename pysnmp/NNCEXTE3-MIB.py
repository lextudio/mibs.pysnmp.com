# SNMP MIB module (NNCEXTE3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NNCEXTE3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:18 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(nncExtensions,) = mibBuilder.importSymbols(
    "NNCGNI0001-SMI",
    "nncExtensions")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

nncExtE3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 40)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NncExtE3Objects_ObjectIdentity = ObjectIdentity
nncExtE3Objects = _NncExtE3Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 1)
)
_NncExtE3Current15MinTable_Object = MibTable
nncExtE3Current15MinTable = _NncExtE3Current15MinTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 1)
)
if mibBuilder.loadTexts:
    nncExtE3Current15MinTable.setStatus("current")
_NncExtE3Current15MinEntry_Object = MibTableRow
nncExtE3Current15MinEntry = _NncExtE3Current15MinEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 1, 1)
)
nncExtE3Current15MinEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nncExtE3Current15MinEntry.setStatus("current")
_NncExtE3Current15MinESs_Type = Gauge32
_NncExtE3Current15MinESs_Object = MibTableColumn
nncExtE3Current15MinESs = _NncExtE3Current15MinESs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 1, 1, 1),
    _NncExtE3Current15MinESs_Type()
)
nncExtE3Current15MinESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtE3Current15MinESs.setStatus("current")
_NncExtE3Current15MinSESs_Type = Gauge32
_NncExtE3Current15MinSESs_Object = MibTableColumn
nncExtE3Current15MinSESs = _NncExtE3Current15MinSESs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 1, 1, 2),
    _NncExtE3Current15MinSESs_Type()
)
nncExtE3Current15MinSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtE3Current15MinSESs.setStatus("current")
_NncExtE3Current15MinSEFs_Type = Gauge32
_NncExtE3Current15MinSEFs_Object = MibTableColumn
nncExtE3Current15MinSEFs = _NncExtE3Current15MinSEFs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 1, 1, 3),
    _NncExtE3Current15MinSEFs_Type()
)
nncExtE3Current15MinSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtE3Current15MinSEFs.setStatus("current")
_NncExtE3Interval15MinTable_Object = MibTable
nncExtE3Interval15MinTable = _NncExtE3Interval15MinTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 2)
)
if mibBuilder.loadTexts:
    nncExtE3Interval15MinTable.setStatus("current")
_NncExtE3Interval15MinEntry_Object = MibTableRow
nncExtE3Interval15MinEntry = _NncExtE3Interval15MinEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 2, 1)
)
nncExtE3Interval15MinEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "NNCEXTE3-MIB", "nncExtE3Interval15MinNumber"),
)
if mibBuilder.loadTexts:
    nncExtE3Interval15MinEntry.setStatus("current")


class _NncExtE3Interval15MinNumber_Type(Integer32):
    """Custom type nncExtE3Interval15MinNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_NncExtE3Interval15MinNumber_Type.__name__ = "Integer32"
_NncExtE3Interval15MinNumber_Object = MibTableColumn
nncExtE3Interval15MinNumber = _NncExtE3Interval15MinNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 2, 1, 1),
    _NncExtE3Interval15MinNumber_Type()
)
nncExtE3Interval15MinNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncExtE3Interval15MinNumber.setStatus("current")
_NncExtE3Interval15MinESs_Type = Gauge32
_NncExtE3Interval15MinESs_Object = MibTableColumn
nncExtE3Interval15MinESs = _NncExtE3Interval15MinESs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 2, 1, 2),
    _NncExtE3Interval15MinESs_Type()
)
nncExtE3Interval15MinESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtE3Interval15MinESs.setStatus("current")
_NncExtE3Interval15MinSESs_Type = Gauge32
_NncExtE3Interval15MinSESs_Object = MibTableColumn
nncExtE3Interval15MinSESs = _NncExtE3Interval15MinSESs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 2, 1, 3),
    _NncExtE3Interval15MinSESs_Type()
)
nncExtE3Interval15MinSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtE3Interval15MinSESs.setStatus("current")
_NncExtE3Interval15MinSEFs_Type = Gauge32
_NncExtE3Interval15MinSEFs_Object = MibTableColumn
nncExtE3Interval15MinSEFs = _NncExtE3Interval15MinSEFs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 2, 1, 4),
    _NncExtE3Interval15MinSEFs_Type()
)
nncExtE3Interval15MinSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtE3Interval15MinSEFs.setStatus("current")
_NncExtE3Total24HrTable_Object = MibTable
nncExtE3Total24HrTable = _NncExtE3Total24HrTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 3)
)
if mibBuilder.loadTexts:
    nncExtE3Total24HrTable.setStatus("current")
_NncExtE3Total24HrEntry_Object = MibTableRow
nncExtE3Total24HrEntry = _NncExtE3Total24HrEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 3, 1)
)
nncExtE3Total24HrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nncExtE3Total24HrEntry.setStatus("current")
_NncExtE3Total24HrESs_Type = Gauge32
_NncExtE3Total24HrESs_Object = MibTableColumn
nncExtE3Total24HrESs = _NncExtE3Total24HrESs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 3, 1, 1),
    _NncExtE3Total24HrESs_Type()
)
nncExtE3Total24HrESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtE3Total24HrESs.setStatus("current")
_NncExtE3Total24HrSESs_Type = Gauge32
_NncExtE3Total24HrSESs_Object = MibTableColumn
nncExtE3Total24HrSESs = _NncExtE3Total24HrSESs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 3, 1, 2),
    _NncExtE3Total24HrSESs_Type()
)
nncExtE3Total24HrSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtE3Total24HrSESs.setStatus("current")
_NncExtE3Total24HrSEFs_Type = Gauge32
_NncExtE3Total24HrSEFs_Object = MibTableColumn
nncExtE3Total24HrSEFs = _NncExtE3Total24HrSEFs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 3, 1, 3),
    _NncExtE3Total24HrSEFs_Type()
)
nncExtE3Total24HrSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtE3Total24HrSEFs.setStatus("current")
_NncExtE3FarEndCurrent15MinTable_Object = MibTable
nncExtE3FarEndCurrent15MinTable = _NncExtE3FarEndCurrent15MinTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 4)
)
if mibBuilder.loadTexts:
    nncExtE3FarEndCurrent15MinTable.setStatus("current")
_NncExtE3FarEndCurrent15MinEntry_Object = MibTableRow
nncExtE3FarEndCurrent15MinEntry = _NncExtE3FarEndCurrent15MinEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 4, 1)
)
nncExtE3FarEndCurrent15MinEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nncExtE3FarEndCurrent15MinEntry.setStatus("current")
_NncExtE3FarEndCurrent15MinFEBEs_Type = Gauge32
_NncExtE3FarEndCurrent15MinFEBEs_Object = MibTableColumn
nncExtE3FarEndCurrent15MinFEBEs = _NncExtE3FarEndCurrent15MinFEBEs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 4, 1, 1),
    _NncExtE3FarEndCurrent15MinFEBEs_Type()
)
nncExtE3FarEndCurrent15MinFEBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtE3FarEndCurrent15MinFEBEs.setStatus("current")
_NncExtE3FarEndCurrent15MinESs_Type = Gauge32
_NncExtE3FarEndCurrent15MinESs_Object = MibTableColumn
nncExtE3FarEndCurrent15MinESs = _NncExtE3FarEndCurrent15MinESs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 4, 1, 2),
    _NncExtE3FarEndCurrent15MinESs_Type()
)
nncExtE3FarEndCurrent15MinESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtE3FarEndCurrent15MinESs.setStatus("current")
_NncExtE3FarEndCurrent15MinSESs_Type = Gauge32
_NncExtE3FarEndCurrent15MinSESs_Object = MibTableColumn
nncExtE3FarEndCurrent15MinSESs = _NncExtE3FarEndCurrent15MinSESs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 4, 1, 3),
    _NncExtE3FarEndCurrent15MinSESs_Type()
)
nncExtE3FarEndCurrent15MinSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtE3FarEndCurrent15MinSESs.setStatus("current")
_NncExtE3FarEndInterval15MinTable_Object = MibTable
nncExtE3FarEndInterval15MinTable = _NncExtE3FarEndInterval15MinTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 5)
)
if mibBuilder.loadTexts:
    nncExtE3FarEndInterval15MinTable.setStatus("current")
_NncExtE3FarEndInterval15MinEntry_Object = MibTableRow
nncExtE3FarEndInterval15MinEntry = _NncExtE3FarEndInterval15MinEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 5, 1)
)
nncExtE3FarEndInterval15MinEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "NNCEXTE3-MIB", "nncExtE3FarEndInterval15MinNumber"),
)
if mibBuilder.loadTexts:
    nncExtE3FarEndInterval15MinEntry.setStatus("current")


class _NncExtE3FarEndInterval15MinNumber_Type(Integer32):
    """Custom type nncExtE3FarEndInterval15MinNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_NncExtE3FarEndInterval15MinNumber_Type.__name__ = "Integer32"
_NncExtE3FarEndInterval15MinNumber_Object = MibTableColumn
nncExtE3FarEndInterval15MinNumber = _NncExtE3FarEndInterval15MinNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 5, 1, 1),
    _NncExtE3FarEndInterval15MinNumber_Type()
)
nncExtE3FarEndInterval15MinNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nncExtE3FarEndInterval15MinNumber.setStatus("current")
_NncExtE3FarEndInterval15MinFEBEs_Type = Gauge32
_NncExtE3FarEndInterval15MinFEBEs_Object = MibTableColumn
nncExtE3FarEndInterval15MinFEBEs = _NncExtE3FarEndInterval15MinFEBEs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 5, 1, 2),
    _NncExtE3FarEndInterval15MinFEBEs_Type()
)
nncExtE3FarEndInterval15MinFEBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtE3FarEndInterval15MinFEBEs.setStatus("current")
_NncExtE3FarEndInterval15MinESs_Type = Gauge32
_NncExtE3FarEndInterval15MinESs_Object = MibTableColumn
nncExtE3FarEndInterval15MinESs = _NncExtE3FarEndInterval15MinESs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 5, 1, 3),
    _NncExtE3FarEndInterval15MinESs_Type()
)
nncExtE3FarEndInterval15MinESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtE3FarEndInterval15MinESs.setStatus("current")
_NncExtE3FarEndInterval15MinSESs_Type = Gauge32
_NncExtE3FarEndInterval15MinSESs_Object = MibTableColumn
nncExtE3FarEndInterval15MinSESs = _NncExtE3FarEndInterval15MinSESs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 5, 1, 4),
    _NncExtE3FarEndInterval15MinSESs_Type()
)
nncExtE3FarEndInterval15MinSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtE3FarEndInterval15MinSESs.setStatus("current")
_NncExtE3FarEndTotal24HrTable_Object = MibTable
nncExtE3FarEndTotal24HrTable = _NncExtE3FarEndTotal24HrTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 6)
)
if mibBuilder.loadTexts:
    nncExtE3FarEndTotal24HrTable.setStatus("current")
_NncExtE3FarEndTotal24HrEntry_Object = MibTableRow
nncExtE3FarEndTotal24HrEntry = _NncExtE3FarEndTotal24HrEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 6, 1)
)
nncExtE3FarEndTotal24HrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nncExtE3FarEndTotal24HrEntry.setStatus("current")
_NncExtE3FarEndTotal24HrFEBEs_Type = Gauge32
_NncExtE3FarEndTotal24HrFEBEs_Object = MibTableColumn
nncExtE3FarEndTotal24HrFEBEs = _NncExtE3FarEndTotal24HrFEBEs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 6, 1, 1),
    _NncExtE3FarEndTotal24HrFEBEs_Type()
)
nncExtE3FarEndTotal24HrFEBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtE3FarEndTotal24HrFEBEs.setStatus("current")
_NncExtE3FarEndTotal24HrESs_Type = Gauge32
_NncExtE3FarEndTotal24HrESs_Object = MibTableColumn
nncExtE3FarEndTotal24HrESs = _NncExtE3FarEndTotal24HrESs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 6, 1, 2),
    _NncExtE3FarEndTotal24HrESs_Type()
)
nncExtE3FarEndTotal24HrESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtE3FarEndTotal24HrESs.setStatus("current")
_NncExtE3FarEndTotal24HrSESs_Type = Gauge32
_NncExtE3FarEndTotal24HrSESs_Object = MibTableColumn
nncExtE3FarEndTotal24HrSESs = _NncExtE3FarEndTotal24HrSESs_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 1, 6, 1, 3),
    _NncExtE3FarEndTotal24HrSESs_Type()
)
nncExtE3FarEndTotal24HrSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtE3FarEndTotal24HrSESs.setStatus("current")
_NncExtE3Traps_ObjectIdentity = ObjectIdentity
nncExtE3Traps = _NncExtE3Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 2)
)
_NncExtE3Groups_ObjectIdentity = ObjectIdentity
nncExtE3Groups = _NncExtE3Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 3)
)
_NncExtE3Compliances_ObjectIdentity = ObjectIdentity
nncExtE3Compliances = _NncExtE3Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 4)
)

# Managed Objects groups

nncExtE3Current15MinGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 3, 1)
)
nncExtE3Current15MinGroup.setObjects(
      *(("NNCEXTE3-MIB", "nncExtE3Current15MinESs"),
        ("NNCEXTE3-MIB", "nncExtE3Current15MinSESs"),
        ("NNCEXTE3-MIB", "nncExtE3Current15MinSEFs"))
)
if mibBuilder.loadTexts:
    nncExtE3Current15MinGroup.setStatus("current")

nncExtE3Interval15MinGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 3, 2)
)
nncExtE3Interval15MinGroup.setObjects(
      *(("NNCEXTE3-MIB", "nncExtE3Interval15MinNumber"),
        ("NNCEXTE3-MIB", "nncExtE3Interval15MinESs"),
        ("NNCEXTE3-MIB", "nncExtE3Interval15MinSESs"),
        ("NNCEXTE3-MIB", "nncExtE3Interval15MinSEFs"))
)
if mibBuilder.loadTexts:
    nncExtE3Interval15MinGroup.setStatus("current")

nncExtE3Total24HrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 3, 3)
)
nncExtE3Total24HrGroup.setObjects(
      *(("NNCEXTE3-MIB", "nncExtE3Total24HrESs"),
        ("NNCEXTE3-MIB", "nncExtE3Total24HrSESs"),
        ("NNCEXTE3-MIB", "nncExtE3Total24HrSEFs"))
)
if mibBuilder.loadTexts:
    nncExtE3Total24HrGroup.setStatus("current")

nncExtE3FarEndCurrent15MinGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 3, 4)
)
nncExtE3FarEndCurrent15MinGroup.setObjects(
      *(("NNCEXTE3-MIB", "nncExtE3FarEndCurrent15MinFEBEs"),
        ("NNCEXTE3-MIB", "nncExtE3FarEndCurrent15MinESs"),
        ("NNCEXTE3-MIB", "nncExtE3FarEndCurrent15MinSESs"))
)
if mibBuilder.loadTexts:
    nncExtE3FarEndCurrent15MinGroup.setStatus("current")

nncExtE3FarEndInterval15MinGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 3, 5)
)
nncExtE3FarEndInterval15MinGroup.setObjects(
      *(("NNCEXTE3-MIB", "nncExtE3FarEndInterval15MinNumber"),
        ("NNCEXTE3-MIB", "nncExtE3FarEndInterval15MinFEBEs"),
        ("NNCEXTE3-MIB", "nncExtE3FarEndInterval15MinESs"),
        ("NNCEXTE3-MIB", "nncExtE3FarEndInterval15MinSESs"))
)
if mibBuilder.loadTexts:
    nncExtE3FarEndInterval15MinGroup.setStatus("current")

nncExtE3FarEndTotal24HrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 3, 6)
)
nncExtE3FarEndTotal24HrGroup.setObjects(
      *(("NNCEXTE3-MIB", "nncExtE3FarEndTotal24HrFEBEs"),
        ("NNCEXTE3-MIB", "nncExtE3FarEndTotal24HrESs"),
        ("NNCEXTE3-MIB", "nncExtE3FarEndTotal24HrSESs"))
)
if mibBuilder.loadTexts:
    nncExtE3FarEndTotal24HrGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

nncExtE3Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 123, 3, 40, 4, 1)
)
if mibBuilder.loadTexts:
    nncExtE3Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NNCEXTE3-MIB",
    **{"nncExtE3": nncExtE3,
       "nncExtE3Objects": nncExtE3Objects,
       "nncExtE3Current15MinTable": nncExtE3Current15MinTable,
       "nncExtE3Current15MinEntry": nncExtE3Current15MinEntry,
       "nncExtE3Current15MinESs": nncExtE3Current15MinESs,
       "nncExtE3Current15MinSESs": nncExtE3Current15MinSESs,
       "nncExtE3Current15MinSEFs": nncExtE3Current15MinSEFs,
       "nncExtE3Interval15MinTable": nncExtE3Interval15MinTable,
       "nncExtE3Interval15MinEntry": nncExtE3Interval15MinEntry,
       "nncExtE3Interval15MinNumber": nncExtE3Interval15MinNumber,
       "nncExtE3Interval15MinESs": nncExtE3Interval15MinESs,
       "nncExtE3Interval15MinSESs": nncExtE3Interval15MinSESs,
       "nncExtE3Interval15MinSEFs": nncExtE3Interval15MinSEFs,
       "nncExtE3Total24HrTable": nncExtE3Total24HrTable,
       "nncExtE3Total24HrEntry": nncExtE3Total24HrEntry,
       "nncExtE3Total24HrESs": nncExtE3Total24HrESs,
       "nncExtE3Total24HrSESs": nncExtE3Total24HrSESs,
       "nncExtE3Total24HrSEFs": nncExtE3Total24HrSEFs,
       "nncExtE3FarEndCurrent15MinTable": nncExtE3FarEndCurrent15MinTable,
       "nncExtE3FarEndCurrent15MinEntry": nncExtE3FarEndCurrent15MinEntry,
       "nncExtE3FarEndCurrent15MinFEBEs": nncExtE3FarEndCurrent15MinFEBEs,
       "nncExtE3FarEndCurrent15MinESs": nncExtE3FarEndCurrent15MinESs,
       "nncExtE3FarEndCurrent15MinSESs": nncExtE3FarEndCurrent15MinSESs,
       "nncExtE3FarEndInterval15MinTable": nncExtE3FarEndInterval15MinTable,
       "nncExtE3FarEndInterval15MinEntry": nncExtE3FarEndInterval15MinEntry,
       "nncExtE3FarEndInterval15MinNumber": nncExtE3FarEndInterval15MinNumber,
       "nncExtE3FarEndInterval15MinFEBEs": nncExtE3FarEndInterval15MinFEBEs,
       "nncExtE3FarEndInterval15MinESs": nncExtE3FarEndInterval15MinESs,
       "nncExtE3FarEndInterval15MinSESs": nncExtE3FarEndInterval15MinSESs,
       "nncExtE3FarEndTotal24HrTable": nncExtE3FarEndTotal24HrTable,
       "nncExtE3FarEndTotal24HrEntry": nncExtE3FarEndTotal24HrEntry,
       "nncExtE3FarEndTotal24HrFEBEs": nncExtE3FarEndTotal24HrFEBEs,
       "nncExtE3FarEndTotal24HrESs": nncExtE3FarEndTotal24HrESs,
       "nncExtE3FarEndTotal24HrSESs": nncExtE3FarEndTotal24HrSESs,
       "nncExtE3Traps": nncExtE3Traps,
       "nncExtE3Groups": nncExtE3Groups,
       "nncExtE3Current15MinGroup": nncExtE3Current15MinGroup,
       "nncExtE3Interval15MinGroup": nncExtE3Interval15MinGroup,
       "nncExtE3Total24HrGroup": nncExtE3Total24HrGroup,
       "nncExtE3FarEndCurrent15MinGroup": nncExtE3FarEndCurrent15MinGroup,
       "nncExtE3FarEndInterval15MinGroup": nncExtE3FarEndInterval15MinGroup,
       "nncExtE3FarEndTotal24HrGroup": nncExtE3FarEndTotal24HrGroup,
       "nncExtE3Compliances": nncExtE3Compliances,
       "nncExtE3Compliance": nncExtE3Compliance}
)
