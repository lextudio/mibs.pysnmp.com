# SNMP MIB module (ZYXEL-DVMRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-DVMRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:38 2024
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

(zyRouteDomainIpAddress,
 zyRouteDomainIpMaskBits) = mibBuilder.importSymbols(
    "ZYXEL-IP-FORWARD-MIB",
    "zyRouteDomainIpAddress",
    "zyRouteDomainIpMaskBits")


# MODULE-IDENTITY

zyxelDvmrp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 23)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelDvmrpSetup_ObjectIdentity = ObjectIdentity
zyxelDvmrpSetup = _ZyxelDvmrpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 23, 1)
)
_ZyDvmrpState_Type = EnabledStatus
_ZyDvmrpState_Object = MibScalar
zyDvmrpState = _ZyDvmrpState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 23, 1, 1),
    _ZyDvmrpState_Type()
)
zyDvmrpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDvmrpState.setStatus("current")
_ZyDvmrpThreshold_Type = Integer32
_ZyDvmrpThreshold_Object = MibScalar
zyDvmrpThreshold = _ZyDvmrpThreshold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 23, 1, 2),
    _ZyDvmrpThreshold_Type()
)
zyDvmrpThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDvmrpThreshold.setStatus("current")
_ZyxelDvmrpRouteDomainTable_Object = MibTable
zyxelDvmrpRouteDomainTable = _ZyxelDvmrpRouteDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 23, 1, 3)
)
if mibBuilder.loadTexts:
    zyxelDvmrpRouteDomainTable.setStatus("current")
_ZyxelDvmrpRouteDomainEntry_Object = MibTableRow
zyxelDvmrpRouteDomainEntry = _ZyxelDvmrpRouteDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 23, 1, 3, 1)
)
zyxelDvmrpRouteDomainEntry.setIndexNames(
    (0, "ZYXEL-IP-FORWARD-MIB", "zyRouteDomainIpAddress"),
    (0, "ZYXEL-IP-FORWARD-MIB", "zyRouteDomainIpMaskBits"),
)
if mibBuilder.loadTexts:
    zyxelDvmrpRouteDomainEntry.setStatus("current")
_ZyDvmrpRouteDomainState_Type = EnabledStatus
_ZyDvmrpRouteDomainState_Object = MibTableColumn
zyDvmrpRouteDomainState = _ZyDvmrpRouteDomainState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 23, 1, 3, 1, 1),
    _ZyDvmrpRouteDomainState_Type()
)
zyDvmrpRouteDomainState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDvmrpRouteDomainState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-DVMRP-MIB",
    **{"zyxelDvmrp": zyxelDvmrp,
       "zyxelDvmrpSetup": zyxelDvmrpSetup,
       "zyDvmrpState": zyDvmrpState,
       "zyDvmrpThreshold": zyDvmrpThreshold,
       "zyxelDvmrpRouteDomainTable": zyxelDvmrpRouteDomainTable,
       "zyxelDvmrpRouteDomainEntry": zyxelDvmrpRouteDomainEntry,
       "zyDvmrpRouteDomainState": zyDvmrpRouteDomainState}
)
