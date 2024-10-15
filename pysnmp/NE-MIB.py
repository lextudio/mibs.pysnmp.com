# SNMP MIB module (NE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:17 2024
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

(ne,) = mibBuilder.importSymbols(
    "CORIOLIS-MIB",
    "ne")

(logRingVPortNo,
 phyRingPortNo,
 phyRingSlotNo) = mibBuilder.importSymbols(
    "RING-MIB",
    "logRingVPortNo",
    "phyRingPortNo",
    "phyRingSlotNo")

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

neMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5812, 5, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfgNeTable_Object = MibTable
cfgNeTable = _CfgNeTable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 5, 1)
)
if mibBuilder.loadTexts:
    cfgNeTable.setStatus("current")
_CfgNeEntry_Object = MibTableRow
cfgNeEntry = _CfgNeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5812, 5, 1, 1)
)
cfgNeEntry.setIndexNames(
    (0, "NE-MIB", "cfgNeIPAddr"),
)
if mibBuilder.loadTexts:
    cfgNeEntry.setStatus("current")
_CfgNeIPAddr_Type = IpAddress
_CfgNeIPAddr_Object = MibTableColumn
cfgNeIPAddr = _CfgNeIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 5812, 5, 1, 1, 1),
    _CfgNeIPAddr_Type()
)
cfgNeIPAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfgNeIPAddr.setStatus("current")


class _CfgNePriMacAddr_Type(OctetString):
    """Custom type cfgNePriMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_CfgNePriMacAddr_Type.__name__ = "OctetString"
_CfgNePriMacAddr_Object = MibTableColumn
cfgNePriMacAddr = _CfgNePriMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 5812, 5, 1, 1, 2),
    _CfgNePriMacAddr_Type()
)
cfgNePriMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNePriMacAddr.setStatus("current")


class _CfgNeSecMacAddr_Type(OctetString):
    """Custom type cfgNeSecMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_CfgNeSecMacAddr_Type.__name__ = "OctetString"
_CfgNeSecMacAddr_Object = MibTableColumn
cfgNeSecMacAddr = _CfgNeSecMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 5812, 5, 1, 1, 3),
    _CfgNeSecMacAddr_Type()
)
cfgNeSecMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNeSecMacAddr.setStatus("current")


class _CfgNeSpareMacAddr_Type(OctetString):
    """Custom type cfgNeSpareMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_CfgNeSpareMacAddr_Type.__name__ = "OctetString"
_CfgNeSpareMacAddr_Object = MibTableColumn
cfgNeSpareMacAddr = _CfgNeSpareMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 5812, 5, 1, 1, 4),
    _CfgNeSpareMacAddr_Type()
)
cfgNeSpareMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgNeSpareMacAddr.setStatus("current")
_NeReachTable_Object = MibTable
neReachTable = _NeReachTable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 5, 3)
)
if mibBuilder.loadTexts:
    neReachTable.setStatus("current")
_NeReachEntry_Object = MibTableRow
neReachEntry = _NeReachEntry_Object(
    (1, 3, 6, 1, 4, 1, 5812, 5, 3, 1)
)
neReachEntry.setIndexNames(
    (0, "NE-MIB", "neReachIpAddr"),
    (0, "RING-MIB", "phyRingSlotNo"),
    (0, "RING-MIB", "phyRingPortNo"),
    (0, "RING-MIB", "logRingVPortNo"),
)
if mibBuilder.loadTexts:
    neReachEntry.setStatus("current")
_NeReachIpAddr_Type = IpAddress
_NeReachIpAddr_Object = MibTableColumn
neReachIpAddr = _NeReachIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5812, 5, 3, 1, 1),
    _NeReachIpAddr_Type()
)
neReachIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neReachIpAddr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NE-MIB",
    **{"cfgNeTable": cfgNeTable,
       "cfgNeEntry": cfgNeEntry,
       "cfgNeIPAddr": cfgNeIPAddr,
       "cfgNePriMacAddr": cfgNePriMacAddr,
       "cfgNeSecMacAddr": cfgNeSecMacAddr,
       "cfgNeSpareMacAddr": cfgNeSpareMacAddr,
       "neMIB": neMIB,
       "neReachTable": neReachTable,
       "neReachEntry": neReachEntry,
       "neReachIpAddr": neReachIpAddr}
)
