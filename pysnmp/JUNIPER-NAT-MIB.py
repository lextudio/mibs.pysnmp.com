# SNMP MIB module (JUNIPER-NAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-NAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:57 2024
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

(InetAddress,
 InetAddressIPv4,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressType")

(jnxSvcsMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxSvcsMibRoot")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

jnxNatMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1)
)
jnxNatMIB.setRevisions(
        ("2010-07-12 20:22",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxNatNotifications_ObjectIdentity = ObjectIdentity
jnxNatNotifications = _JnxNatNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 0)
)
_JnxNatObjects_ObjectIdentity = ObjectIdentity
jnxNatObjects = _JnxNatObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1)
)
_JnxSrcNatStatsTable_Object = MibTable
jnxSrcNatStatsTable = _JnxSrcNatStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxSrcNatStatsTable.setStatus("current")
_JnxSrcNatStatsEntry_Object = MibTableRow
jnxSrcNatStatsEntry = _JnxSrcNatStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 1, 1)
)
jnxSrcNatStatsEntry.setIndexNames(
    (0, "JUNIPER-NAT-MIB", "jnxNatSrcPoolName"),
)
if mibBuilder.loadTexts:
    jnxSrcNatStatsEntry.setStatus("current")


class _JnxNatSrcPoolName_Type(DisplayString):
    """Custom type jnxNatSrcPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxNatSrcPoolName_Type.__name__ = "DisplayString"
_JnxNatSrcPoolName_Object = MibTableColumn
jnxNatSrcPoolName = _JnxNatSrcPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 1, 1, 1),
    _JnxNatSrcPoolName_Type()
)
jnxNatSrcPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxNatSrcPoolName.setStatus("current")


class _JnxNatSrcXlatedAddrType_Type(Integer32):
    """Custom type jnxNatSrcXlatedAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_JnxNatSrcXlatedAddrType_Type.__name__ = "Integer32"
_JnxNatSrcXlatedAddrType_Object = MibTableColumn
jnxNatSrcXlatedAddrType = _JnxNatSrcXlatedAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 1, 1, 2),
    _JnxNatSrcXlatedAddrType_Type()
)
jnxNatSrcXlatedAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxNatSrcXlatedAddrType.setStatus("current")


class _JnxNatSrcPoolType_Type(Integer32):
    """Custom type jnxNatSrcPoolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
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
              26)
        )
    )
    namedValues = NamedValues(
        *(("basic-nat-pt", 17),
          ("basic-nat44", 11),
          ("basic-nat66", 19),
          ("det-napt44", 25),
          ("dnat-44", 14),
          ("dynamic-napt", 2),
          ("dynamic-nat", 3),
          ("dynamic-nat44", 12),
          ("napt-44", 13),
          ("napt-66", 21),
          ("napt-pt", 18),
          ("sd-napt44", 26),
          ("stateful-nat64", 15),
          ("stateless-nat64", 16),
          ("stateless-nat66", 20),
          ("static", 1),
          ("twice-basic-nat-44", 23),
          ("twice-dynamic-nat-44", 24),
          ("twice-napt-44", 22))
    )


_JnxNatSrcPoolType_Type.__name__ = "Integer32"
_JnxNatSrcPoolType_Object = MibTableColumn
jnxNatSrcPoolType = _JnxNatSrcPoolType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 1, 1, 3),
    _JnxNatSrcPoolType_Type()
)
jnxNatSrcPoolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxNatSrcPoolType.setStatus("current")
_JnxNatSrcNumPortAvail_Type = Unsigned32
_JnxNatSrcNumPortAvail_Object = MibTableColumn
jnxNatSrcNumPortAvail = _JnxNatSrcNumPortAvail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 1, 1, 4),
    _JnxNatSrcNumPortAvail_Type()
)
jnxNatSrcNumPortAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxNatSrcNumPortAvail.setStatus("current")
_JnxNatSrcNumPortInuse_Type = Unsigned32
_JnxNatSrcNumPortInuse_Object = MibTableColumn
jnxNatSrcNumPortInuse = _JnxNatSrcNumPortInuse_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 1, 1, 5),
    _JnxNatSrcNumPortInuse_Type()
)
jnxNatSrcNumPortInuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxNatSrcNumPortInuse.setStatus("current")
_JnxNatSrcNumAddressAvail_Type = Unsigned32
_JnxNatSrcNumAddressAvail_Object = MibTableColumn
jnxNatSrcNumAddressAvail = _JnxNatSrcNumAddressAvail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 1, 1, 6),
    _JnxNatSrcNumAddressAvail_Type()
)
jnxNatSrcNumAddressAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxNatSrcNumAddressAvail.setStatus("current")
_JnxNatSrcNumAddressInUse_Type = Unsigned32
_JnxNatSrcNumAddressInUse_Object = MibTableColumn
jnxNatSrcNumAddressInUse = _JnxNatSrcNumAddressInUse_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 1, 1, 7),
    _JnxNatSrcNumAddressInUse_Type()
)
jnxNatSrcNumAddressInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxNatSrcNumAddressInUse.setStatus("current")
_JnxNatSrcNumSessions_Type = Unsigned32
_JnxNatSrcNumSessions_Object = MibTableColumn
jnxNatSrcNumSessions = _JnxNatSrcNumSessions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 1, 1, 8),
    _JnxNatSrcNumSessions_Type()
)
jnxNatSrcNumSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxNatSrcNumSessions.setStatus("current")
_JnxNatRuleTable_Object = MibTable
jnxNatRuleTable = _JnxNatRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 2)
)
if mibBuilder.loadTexts:
    jnxNatRuleTable.setStatus("current")
_JnxNatRuleEntry_Object = MibTableRow
jnxNatRuleEntry = _JnxNatRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 2, 1)
)
jnxNatRuleEntry.setIndexNames(
    (0, "JUNIPER-NAT-MIB", "jnxNatRuleName"),
)
if mibBuilder.loadTexts:
    jnxNatRuleEntry.setStatus("current")


class _JnxNatRuleName_Type(DisplayString):
    """Custom type jnxNatRuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_JnxNatRuleName_Type.__name__ = "DisplayString"
_JnxNatRuleName_Object = MibTableColumn
jnxNatRuleName = _JnxNatRuleName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 2, 1, 1),
    _JnxNatRuleName_Type()
)
jnxNatRuleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxNatRuleName.setStatus("current")


class _JnxNatRuleType_Type(Integer32):
    """Custom type jnxNatRuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
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
              26)
        )
    )
    namedValues = NamedValues(
        *(("basic-nat-pt", 17),
          ("basic-nat44", 11),
          ("basic-nat66", 19),
          ("det-napt44", 25),
          ("dnat-44", 14),
          ("dynamic-nat44", 12),
          ("dynamic-source", 3),
          ("napt", 4),
          ("napt-44", 13),
          ("napt-66", 21),
          ("napt-pt", 18),
          ("sd-napt44", 26),
          ("stateful-nat64", 15),
          ("stateless-nat64", 16),
          ("stateless-nat66", 20),
          ("static-destination", 2),
          ("static-source", 1),
          ("twice-basic-nat-44", 23),
          ("twice-dynamic-nat-44", 24),
          ("twice-napt-44", 22))
    )


_JnxNatRuleType_Type.__name__ = "Integer32"
_JnxNatRuleType_Object = MibTableColumn
jnxNatRuleType = _JnxNatRuleType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 2, 1, 2),
    _JnxNatRuleType_Type()
)
jnxNatRuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxNatRuleType.setStatus("current")
_JnxNatRuleTransHits_Type = Unsigned32
_JnxNatRuleTransHits_Object = MibTableColumn
jnxNatRuleTransHits = _JnxNatRuleTransHits_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 2, 1, 3),
    _JnxNatRuleTransHits_Type()
)
jnxNatRuleTransHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxNatRuleTransHits.setStatus("current")
_JnxNatPoolTable_Object = MibTable
jnxNatPoolTable = _JnxNatPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 3)
)
if mibBuilder.loadTexts:
    jnxNatPoolTable.setStatus("current")
_JnxNatPoolEntry_Object = MibTableRow
jnxNatPoolEntry = _JnxNatPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 3, 1)
)
jnxNatPoolEntry.setIndexNames(
    (0, "JUNIPER-NAT-MIB", "jnxNatPoolName"),
)
if mibBuilder.loadTexts:
    jnxNatPoolEntry.setStatus("current")


class _JnxNatPoolName_Type(DisplayString):
    """Custom type jnxNatPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxNatPoolName_Type.__name__ = "DisplayString"
_JnxNatPoolName_Object = MibTableColumn
jnxNatPoolName = _JnxNatPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 3, 1, 1),
    _JnxNatPoolName_Type()
)
jnxNatPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxNatPoolName.setStatus("current")


class _JnxNatPoolType_Type(Integer32):
    """Custom type jnxNatPoolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
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
              26)
        )
    )
    namedValues = NamedValues(
        *(("basic-nat-pt", 17),
          ("basic-nat44", 11),
          ("basic-nat66", 19),
          ("det-napt44", 25),
          ("dnat-44", 14),
          ("dynamic-nat44", 12),
          ("dynamic-source", 3),
          ("napt", 4),
          ("napt-44", 13),
          ("napt-66", 21),
          ("napt-pt", 18),
          ("sd-napt44", 26),
          ("stateful-nat64", 15),
          ("stateless-nat64", 16),
          ("stateless-nat66", 20),
          ("static-destination", 2),
          ("static-source", 1),
          ("twice-basic-nat-44", 23),
          ("twice-dynamic-nat-44", 24),
          ("twice-napt-44", 22))
    )


_JnxNatPoolType_Type.__name__ = "Integer32"
_JnxNatPoolType_Object = MibTableColumn
jnxNatPoolType = _JnxNatPoolType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 3, 1, 2),
    _JnxNatPoolType_Type()
)
jnxNatPoolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxNatPoolType.setStatus("current")
_JnxNatPoolTransHits_Type = Unsigned32
_JnxNatPoolTransHits_Object = MibTableColumn
jnxNatPoolTransHits = _JnxNatPoolTransHits_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 3, 1, 3),
    _JnxNatPoolTransHits_Type()
)
jnxNatPoolTransHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxNatPoolTransHits.setStatus("current")
_JnxNatTrapVars_ObjectIdentity = ObjectIdentity
jnxNatTrapVars = _JnxNatTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 2)
)


class _JnxNatAddrPoolUtil_Type(Integer32):
    """Custom type jnxNatAddrPoolUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JnxNatAddrPoolUtil_Type.__name__ = "Integer32"
_JnxNatAddrPoolUtil_Object = MibScalar
jnxNatAddrPoolUtil = _JnxNatAddrPoolUtil_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 2, 1),
    _JnxNatAddrPoolUtil_Type()
)
jnxNatAddrPoolUtil.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxNatAddrPoolUtil.setStatus("current")


class _JnxNatTrapSrcPoolName_Type(DisplayString):
    """Custom type jnxNatTrapSrcPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxNatTrapSrcPoolName_Type.__name__ = "DisplayString"
_JnxNatTrapSrcPoolName_Object = MibScalar
jnxNatTrapSrcPoolName = _JnxNatTrapSrcPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 2, 2),
    _JnxNatTrapSrcPoolName_Type()
)
jnxNatTrapSrcPoolName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxNatTrapSrcPoolName.setStatus("current")

# Managed Objects groups


# Notification objects

jnxNatAddrPoolThresholdStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 0, 1)
)
jnxNatAddrPoolThresholdStatus.setObjects(
      *(("JUNIPER-NAT-MIB", "jnxNatTrapSrcPoolName"),
        ("JUNIPER-NAT-MIB", "jnxNatAddrPoolUtil"))
)
if mibBuilder.loadTexts:
    jnxNatAddrPoolThresholdStatus.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-NAT-MIB",
    **{"jnxNatMIB": jnxNatMIB,
       "jnxNatNotifications": jnxNatNotifications,
       "jnxNatAddrPoolThresholdStatus": jnxNatAddrPoolThresholdStatus,
       "jnxNatObjects": jnxNatObjects,
       "jnxSrcNatStatsTable": jnxSrcNatStatsTable,
       "jnxSrcNatStatsEntry": jnxSrcNatStatsEntry,
       "jnxNatSrcPoolName": jnxNatSrcPoolName,
       "jnxNatSrcXlatedAddrType": jnxNatSrcXlatedAddrType,
       "jnxNatSrcPoolType": jnxNatSrcPoolType,
       "jnxNatSrcNumPortAvail": jnxNatSrcNumPortAvail,
       "jnxNatSrcNumPortInuse": jnxNatSrcNumPortInuse,
       "jnxNatSrcNumAddressAvail": jnxNatSrcNumAddressAvail,
       "jnxNatSrcNumAddressInUse": jnxNatSrcNumAddressInUse,
       "jnxNatSrcNumSessions": jnxNatSrcNumSessions,
       "jnxNatRuleTable": jnxNatRuleTable,
       "jnxNatRuleEntry": jnxNatRuleEntry,
       "jnxNatRuleName": jnxNatRuleName,
       "jnxNatRuleType": jnxNatRuleType,
       "jnxNatRuleTransHits": jnxNatRuleTransHits,
       "jnxNatPoolTable": jnxNatPoolTable,
       "jnxNatPoolEntry": jnxNatPoolEntry,
       "jnxNatPoolName": jnxNatPoolName,
       "jnxNatPoolType": jnxNatPoolType,
       "jnxNatPoolTransHits": jnxNatPoolTransHits,
       "jnxNatTrapVars": jnxNatTrapVars,
       "jnxNatAddrPoolUtil": jnxNatAddrPoolUtil,
       "jnxNatTrapSrcPoolName": jnxNatTrapSrcPoolName}
)
