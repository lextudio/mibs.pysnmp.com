# SNMP MIB module (RADLAN-GMRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-GMRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:42:21 2024
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

rlGmrp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 75)
)
rlGmrp.setRevisions(
        ("2007-01-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlGmrpSupported_Type = TruthValue
_RlGmrpSupported_Object = MibScalar
rlGmrpSupported = _RlGmrpSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 75, 1),
    _RlGmrpSupported_Type()
)
rlGmrpSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlGmrpSupported.setStatus("current")
_RlGmrpMibVersion_Type = Integer32
_RlGmrpMibVersion_Object = MibScalar
rlGmrpMibVersion = _RlGmrpMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 75, 2),
    _RlGmrpMibVersion_Type()
)
rlGmrpMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlGmrpMibVersion.setStatus("current")
_RlPortGmrpTimersTable_Object = MibTable
rlPortGmrpTimersTable = _RlPortGmrpTimersTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 75, 3)
)
if mibBuilder.loadTexts:
    rlPortGmrpTimersTable.setStatus("current")
_RlPortGmrpTimersEntry_Object = MibTableRow
rlPortGmrpTimersEntry = _RlPortGmrpTimersEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 75, 3, 1)
)
rlPortGmrpTimersEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    rlPortGmrpTimersEntry.setStatus("current")


class _RlPortGmrpJoinTime_Type(TimeInterval):
    """Custom type rlPortGmrpJoinTime based on TimeInterval"""
    defaultValue = 20


_RlPortGmrpJoinTime_Object = MibTableColumn
rlPortGmrpJoinTime = _RlPortGmrpJoinTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 75, 3, 1, 1),
    _RlPortGmrpJoinTime_Type()
)
rlPortGmrpJoinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortGmrpJoinTime.setStatus("current")


class _RlPortGmrpLeaveTime_Type(TimeInterval):
    """Custom type rlPortGmrpLeaveTime based on TimeInterval"""
    defaultValue = 60


_RlPortGmrpLeaveTime_Object = MibTableColumn
rlPortGmrpLeaveTime = _RlPortGmrpLeaveTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 75, 3, 1, 2),
    _RlPortGmrpLeaveTime_Type()
)
rlPortGmrpLeaveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortGmrpLeaveTime.setStatus("current")


class _RlPortGmrpLeaveAllTime_Type(TimeInterval):
    """Custom type rlPortGmrpLeaveAllTime based on TimeInterval"""
    defaultValue = 1000


_RlPortGmrpLeaveAllTime_Object = MibTableColumn
rlPortGmrpLeaveAllTime = _RlPortGmrpLeaveAllTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 75, 3, 1, 3),
    _RlPortGmrpLeaveAllTime_Type()
)
rlPortGmrpLeaveAllTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortGmrpLeaveAllTime.setStatus("current")


class _RlPortGmrpOverrideGarp_Type(EnabledStatus):
    """Custom type rlPortGmrpOverrideGarp based on EnabledStatus"""


_RlPortGmrpOverrideGarp_Object = MibTableColumn
rlPortGmrpOverrideGarp = _RlPortGmrpOverrideGarp_Object(
    (1, 3, 6, 1, 4, 1, 89, 75, 3, 1, 4),
    _RlPortGmrpOverrideGarp_Type()
)
rlPortGmrpOverrideGarp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortGmrpOverrideGarp.setStatus("current")
_RlGmrpVlanTable_Object = MibTable
rlGmrpVlanTable = _RlGmrpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 75, 4)
)
if mibBuilder.loadTexts:
    rlGmrpVlanTable.setStatus("current")
_RlGmrpVlanEntry_Object = MibTableRow
rlGmrpVlanEntry = _RlGmrpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 75, 4, 1)
)
rlGmrpVlanEntry.setIndexNames(
    (0, "RADLAN-GMRP-MIB", "rlGmrpVlanTag"),
)
if mibBuilder.loadTexts:
    rlGmrpVlanEntry.setStatus("current")
_RlGmrpVlanTag_Type = Integer32
_RlGmrpVlanTag_Object = MibTableColumn
rlGmrpVlanTag = _RlGmrpVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 75, 4, 1, 1),
    _RlGmrpVlanTag_Type()
)
rlGmrpVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlGmrpVlanTag.setStatus("current")


class _RlGmrpVlanEnable_Type(TruthValue):
    """Custom type rlGmrpVlanEnable based on TruthValue"""


_RlGmrpVlanEnable_Object = MibTableColumn
rlGmrpVlanEnable = _RlGmrpVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 75, 4, 1, 2),
    _RlGmrpVlanEnable_Type()
)
rlGmrpVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlGmrpVlanEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-GMRP-MIB",
    **{"rlGmrp": rlGmrp,
       "rlGmrpSupported": rlGmrpSupported,
       "rlGmrpMibVersion": rlGmrpMibVersion,
       "rlPortGmrpTimersTable": rlPortGmrpTimersTable,
       "rlPortGmrpTimersEntry": rlPortGmrpTimersEntry,
       "rlPortGmrpJoinTime": rlPortGmrpJoinTime,
       "rlPortGmrpLeaveTime": rlPortGmrpLeaveTime,
       "rlPortGmrpLeaveAllTime": rlPortGmrpLeaveAllTime,
       "rlPortGmrpOverrideGarp": rlPortGmrpOverrideGarp,
       "rlGmrpVlanTable": rlGmrpVlanTable,
       "rlGmrpVlanEntry": rlGmrpVlanEntry,
       "rlGmrpVlanTag": rlGmrpVlanTag,
       "rlGmrpVlanEnable": rlGmrpVlanEnable}
)
