# SNMP MIB module (ZYXEL-RATE-LIMIT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-RATE-LIMIT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:42 2024
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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelRateLimit = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 72)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelRateLimitSetup_ObjectIdentity = ObjectIdentity
zyxelRateLimitSetup = _ZyxelRateLimitSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 72, 1)
)
_ZyRateLimitState_Type = EnabledStatus
_ZyRateLimitState_Object = MibScalar
zyRateLimitState = _ZyRateLimitState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 72, 1, 1),
    _ZyRateLimitState_Type()
)
zyRateLimitState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyRateLimitState.setStatus("current")
_ZyxelRateLimitPortTable_Object = MibTable
zyxelRateLimitPortTable = _ZyxelRateLimitPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 72, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelRateLimitPortTable.setStatus("current")
_ZyxelRateLimitPortEntry_Object = MibTableRow
zyxelRateLimitPortEntry = _ZyxelRateLimitPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 72, 1, 2, 1)
)
zyxelRateLimitPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelRateLimitPortEntry.setStatus("current")
_ZyRateLimitPortCommitState_Type = EnabledStatus
_ZyRateLimitPortCommitState_Object = MibTableColumn
zyRateLimitPortCommitState = _ZyRateLimitPortCommitState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 72, 1, 2, 1, 1),
    _ZyRateLimitPortCommitState_Type()
)
zyRateLimitPortCommitState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyRateLimitPortCommitState.setStatus("current")
_ZyRateLimitPortCommitRate_Type = Integer32
_ZyRateLimitPortCommitRate_Object = MibTableColumn
zyRateLimitPortCommitRate = _ZyRateLimitPortCommitRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 72, 1, 2, 1, 2),
    _ZyRateLimitPortCommitRate_Type()
)
zyRateLimitPortCommitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyRateLimitPortCommitRate.setStatus("current")
_ZyRateLimitPortPeakState_Type = EnabledStatus
_ZyRateLimitPortPeakState_Object = MibTableColumn
zyRateLimitPortPeakState = _ZyRateLimitPortPeakState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 72, 1, 2, 1, 3),
    _ZyRateLimitPortPeakState_Type()
)
zyRateLimitPortPeakState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyRateLimitPortPeakState.setStatus("current")
_ZyRateLimitPortPeakRate_Type = Integer32
_ZyRateLimitPortPeakRate_Object = MibTableColumn
zyRateLimitPortPeakRate = _ZyRateLimitPortPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 72, 1, 2, 1, 4),
    _ZyRateLimitPortPeakRate_Type()
)
zyRateLimitPortPeakRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyRateLimitPortPeakRate.setStatus("current")
_ZyRateLimitPortEgressState_Type = EnabledStatus
_ZyRateLimitPortEgressState_Object = MibTableColumn
zyRateLimitPortEgressState = _ZyRateLimitPortEgressState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 72, 1, 2, 1, 5),
    _ZyRateLimitPortEgressState_Type()
)
zyRateLimitPortEgressState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyRateLimitPortEgressState.setStatus("current")
_ZyRateLimitPortEgressRate_Type = Integer32
_ZyRateLimitPortEgressRate_Object = MibTableColumn
zyRateLimitPortEgressRate = _ZyRateLimitPortEgressRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 72, 1, 2, 1, 6),
    _ZyRateLimitPortEgressRate_Type()
)
zyRateLimitPortEgressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyRateLimitPortEgressRate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-RATE-LIMIT-MIB",
    **{"zyxelRateLimit": zyxelRateLimit,
       "zyxelRateLimitSetup": zyxelRateLimitSetup,
       "zyRateLimitState": zyRateLimitState,
       "zyxelRateLimitPortTable": zyxelRateLimitPortTable,
       "zyxelRateLimitPortEntry": zyxelRateLimitPortEntry,
       "zyRateLimitPortCommitState": zyRateLimitPortCommitState,
       "zyRateLimitPortCommitRate": zyRateLimitPortCommitRate,
       "zyRateLimitPortPeakState": zyRateLimitPortPeakState,
       "zyRateLimitPortPeakRate": zyRateLimitPortPeakRate,
       "zyRateLimitPortEgressState": zyRateLimitPortEgressState,
       "zyRateLimitPortEgressRate": zyRateLimitPortEgressRate}
)
