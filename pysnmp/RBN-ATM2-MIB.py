# SNMP MIB module (RBN-ATM2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-ATM2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:56 2024
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

(atmAal5VclStatEntry,
 atmVclStatEntry,
 atmVplStatEntry) = mibBuilder.importSymbols(
    "ATM2-MIB",
    "atmAal5VclStatEntry",
    "atmVclStatEntry",
    "atmVplStatEntry")

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

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

rbnAtm2MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 50)
)
rbnAtm2MIB.setRevisions(
        ("2009-06-11 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnAtm2MIBObjects_ObjectIdentity = ObjectIdentity
rbnAtm2MIBObjects = _RbnAtm2MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 50, 1)
)
_RbnAtm2VplStatTable_Object = MibTable
rbnAtm2VplStatTable = _RbnAtm2VplStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 50, 1, 1)
)
if mibBuilder.loadTexts:
    rbnAtm2VplStatTable.setStatus("current")
_RbnAtm2VplStatEntry_Object = MibTableRow
rbnAtm2VplStatEntry = _RbnAtm2VplStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 50, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rbnAtm2VplStatEntry.setStatus("current")
_RbnAtm2VplOutPktDrops_Type = Counter32
_RbnAtm2VplOutPktDrops_Object = MibTableColumn
rbnAtm2VplOutPktDrops = _RbnAtm2VplOutPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 50, 1, 1, 1, 1),
    _RbnAtm2VplOutPktDrops_Type()
)
rbnAtm2VplOutPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnAtm2VplOutPktDrops.setStatus("current")
_RbnAtm2VclStatTable_Object = MibTable
rbnAtm2VclStatTable = _RbnAtm2VclStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 50, 1, 2)
)
if mibBuilder.loadTexts:
    rbnAtm2VclStatTable.setStatus("current")
_RbnAtm2VclStatEntry_Object = MibTableRow
rbnAtm2VclStatEntry = _RbnAtm2VclStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 50, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rbnAtm2VclStatEntry.setStatus("current")
_RbnAtm2VclOutPktDrops_Type = Counter32
_RbnAtm2VclOutPktDrops_Object = MibTableColumn
rbnAtm2VclOutPktDrops = _RbnAtm2VclOutPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 50, 1, 2, 1, 1),
    _RbnAtm2VclOutPktDrops_Type()
)
rbnAtm2VclOutPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnAtm2VclOutPktDrops.setStatus("current")
_RbnAtm2Aal5VclStatTable_Object = MibTable
rbnAtm2Aal5VclStatTable = _RbnAtm2Aal5VclStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 50, 1, 3)
)
if mibBuilder.loadTexts:
    rbnAtm2Aal5VclStatTable.setStatus("current")
_RbnAtm2Aal5VclStatEntry_Object = MibTableRow
rbnAtm2Aal5VclStatEntry = _RbnAtm2Aal5VclStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 50, 1, 3, 1)
)
if mibBuilder.loadTexts:
    rbnAtm2Aal5VclStatEntry.setStatus("current")
_RbnAtm2Aal5VclOutPktDrops_Type = Counter32
_RbnAtm2Aal5VclOutPktDrops_Object = MibTableColumn
rbnAtm2Aal5VclOutPktDrops = _RbnAtm2Aal5VclOutPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 50, 1, 3, 1, 1),
    _RbnAtm2Aal5VclOutPktDrops_Type()
)
rbnAtm2Aal5VclOutPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnAtm2Aal5VclOutPktDrops.setStatus("current")
_RbnAtm2MIBConformance_ObjectIdentity = ObjectIdentity
rbnAtm2MIBConformance = _RbnAtm2MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 50, 2)
)
_RbnAtm2MIBCompliances_ObjectIdentity = ObjectIdentity
rbnAtm2MIBCompliances = _RbnAtm2MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 50, 2, 1)
)
_RbnAtm2MIBGroups_ObjectIdentity = ObjectIdentity
rbnAtm2MIBGroups = _RbnAtm2MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 50, 2, 2)
)
atmVplStatEntry.registerAugmentions(
    ("RBN-ATM2-MIB",
     "rbnAtm2VplStatEntry")
)
rbnAtm2VplStatEntry.setIndexNames(*atmVplStatEntry.getIndexNames())
atmVclStatEntry.registerAugmentions(
    ("RBN-ATM2-MIB",
     "rbnAtm2VclStatEntry")
)
rbnAtm2VclStatEntry.setIndexNames(*atmVclStatEntry.getIndexNames())
atmAal5VclStatEntry.registerAugmentions(
    ("RBN-ATM2-MIB",
     "rbnAtm2Aal5VclStatEntry")
)
rbnAtm2Aal5VclStatEntry.setIndexNames(*atmAal5VclStatEntry.getIndexNames())

# Managed Objects groups

rbnAtm2CommonStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 50, 2, 2, 1)
)
rbnAtm2CommonStatsGroup.setObjects(
      *(("RBN-ATM2-MIB", "rbnAtm2VplOutPktDrops"),
        ("RBN-ATM2-MIB", "rbnAtm2VclOutPktDrops"))
)
if mibBuilder.loadTexts:
    rbnAtm2CommonStatsGroup.setStatus("current")

rbnAtm2HostGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 50, 2, 2, 2)
)
rbnAtm2HostGroup.setObjects(
    ("RBN-ATM2-MIB", "rbnAtm2Aal5VclOutPktDrops")
)
if mibBuilder.loadTexts:
    rbnAtm2HostGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbnAtm2Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 50, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rbnAtm2Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-ATM2-MIB",
    **{"rbnAtm2MIB": rbnAtm2MIB,
       "rbnAtm2MIBObjects": rbnAtm2MIBObjects,
       "rbnAtm2VplStatTable": rbnAtm2VplStatTable,
       "rbnAtm2VplStatEntry": rbnAtm2VplStatEntry,
       "rbnAtm2VplOutPktDrops": rbnAtm2VplOutPktDrops,
       "rbnAtm2VclStatTable": rbnAtm2VclStatTable,
       "rbnAtm2VclStatEntry": rbnAtm2VclStatEntry,
       "rbnAtm2VclOutPktDrops": rbnAtm2VclOutPktDrops,
       "rbnAtm2Aal5VclStatTable": rbnAtm2Aal5VclStatTable,
       "rbnAtm2Aal5VclStatEntry": rbnAtm2Aal5VclStatEntry,
       "rbnAtm2Aal5VclOutPktDrops": rbnAtm2Aal5VclOutPktDrops,
       "rbnAtm2MIBConformance": rbnAtm2MIBConformance,
       "rbnAtm2MIBCompliances": rbnAtm2MIBCompliances,
       "rbnAtm2Compliance": rbnAtm2Compliance,
       "rbnAtm2MIBGroups": rbnAtm2MIBGroups,
       "rbnAtm2CommonStatsGroup": rbnAtm2CommonStatsGroup,
       "rbnAtm2HostGroup": rbnAtm2HostGroup}
)
