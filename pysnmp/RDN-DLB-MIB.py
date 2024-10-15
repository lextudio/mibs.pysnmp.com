# SNMP MIB module (RDN-DLB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RDN-DLB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:07 2024
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

(riverdelta,) = mibBuilder.importSymbols(
    "RDN-MIB",
    "riverdelta")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rdnLoadBalance = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 8)
)
rdnLoadBalance.setRevisions(
        ("2008-08-08 00:00",
         "2004-09-15 00:00",
         "2004-09-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RdnLoadBalBasicRuleTable_Object = MibTable
rdnLoadBalBasicRuleTable = _RdnLoadBalBasicRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 8, 1)
)
if mibBuilder.loadTexts:
    rdnLoadBalBasicRuleTable.setStatus("current")
_RdnLoadBalBasicRuleEntry_Object = MibTableRow
rdnLoadBalBasicRuleEntry = _RdnLoadBalBasicRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 8, 1, 1)
)
rdnLoadBalBasicRuleEntry.setIndexNames(
    (0, "RDN-DLB-MIB", "rdnLoadBalBasicRuleId"),
)
if mibBuilder.loadTexts:
    rdnLoadBalBasicRuleEntry.setStatus("current")


class _RdnLoadBalBasicRuleId_Type(Unsigned32):
    """Custom type rdnLoadBalBasicRuleId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RdnLoadBalBasicRuleId_Type.__name__ = "Unsigned32"
_RdnLoadBalBasicRuleId_Object = MibTableColumn
rdnLoadBalBasicRuleId = _RdnLoadBalBasicRuleId_Object(
    (1, 3, 6, 1, 4, 1, 4981, 8, 1, 1, 1),
    _RdnLoadBalBasicRuleId_Type()
)
rdnLoadBalBasicRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdnLoadBalBasicRuleId.setStatus("current")


class _RdnLoadBalBasicRuleEnable_Type(Integer32):
    """Custom type rdnLoadBalBasicRuleEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("downstream", 2),
          ("ds-reg", 7),
          ("ds-reg-bonding", 9),
          ("interval", 3),
          ("registration", 4),
          ("rem-dsx", 5),
          ("spec-trig", 6),
          ("upstream", 1),
          ("us-reg-bonding", 8))
    )


_RdnLoadBalBasicRuleEnable_Type.__name__ = "Integer32"
_RdnLoadBalBasicRuleEnable_Object = MibTableColumn
rdnLoadBalBasicRuleEnable = _RdnLoadBalBasicRuleEnable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 8, 1, 1, 2),
    _RdnLoadBalBasicRuleEnable_Type()
)
rdnLoadBalBasicRuleEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnLoadBalBasicRuleEnable.setStatus("current")


class _RdnLoadBalBasicRuleMinThres_Type(Unsigned32):
    """Custom type rdnLoadBalBasicRuleMinThres based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RdnLoadBalBasicRuleMinThres_Type.__name__ = "Unsigned32"
_RdnLoadBalBasicRuleMinThres_Object = MibTableColumn
rdnLoadBalBasicRuleMinThres = _RdnLoadBalBasicRuleMinThres_Object(
    (1, 3, 6, 1, 4, 1, 4981, 8, 1, 1, 3),
    _RdnLoadBalBasicRuleMinThres_Type()
)
rdnLoadBalBasicRuleMinThres.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnLoadBalBasicRuleMinThres.setStatus("current")


class _RdnLoadBalBasicRuleDeltaThres_Type(Unsigned32):
    """Custom type rdnLoadBalBasicRuleDeltaThres based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RdnLoadBalBasicRuleDeltaThres_Type.__name__ = "Unsigned32"
_RdnLoadBalBasicRuleDeltaThres_Object = MibTableColumn
rdnLoadBalBasicRuleDeltaThres = _RdnLoadBalBasicRuleDeltaThres_Object(
    (1, 3, 6, 1, 4, 1, 4981, 8, 1, 1, 4),
    _RdnLoadBalBasicRuleDeltaThres_Type()
)
rdnLoadBalBasicRuleDeltaThres.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnLoadBalBasicRuleDeltaThres.setStatus("current")


class _RdnLoadBalBasicRuleStopThres_Type(Unsigned32):
    """Custom type rdnLoadBalBasicRuleStopThres based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RdnLoadBalBasicRuleStopThres_Type.__name__ = "Unsigned32"
_RdnLoadBalBasicRuleStopThres_Object = MibTableColumn
rdnLoadBalBasicRuleStopThres = _RdnLoadBalBasicRuleStopThres_Object(
    (1, 3, 6, 1, 4, 1, 4981, 8, 1, 1, 5),
    _RdnLoadBalBasicRuleStopThres_Type()
)
rdnLoadBalBasicRuleStopThres.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnLoadBalBasicRuleStopThres.setStatus("current")
_RdnLoadBalBasicRuleRowStatus_Type = RowStatus
_RdnLoadBalBasicRuleRowStatus_Object = MibTableColumn
rdnLoadBalBasicRuleRowStatus = _RdnLoadBalBasicRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4981, 8, 1, 1, 7),
    _RdnLoadBalBasicRuleRowStatus_Type()
)
rdnLoadBalBasicRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnLoadBalBasicRuleRowStatus.setStatus("current")


class _RdnLoadBalBasicRuleModemCountThres_Type(Unsigned32):
    """Custom type rdnLoadBalBasicRuleModemCountThres based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_RdnLoadBalBasicRuleModemCountThres_Type.__name__ = "Unsigned32"
_RdnLoadBalBasicRuleModemCountThres_Object = MibTableColumn
rdnLoadBalBasicRuleModemCountThres = _RdnLoadBalBasicRuleModemCountThres_Object(
    (1, 3, 6, 1, 4, 1, 4981, 8, 1, 1, 8),
    _RdnLoadBalBasicRuleModemCountThres_Type()
)
rdnLoadBalBasicRuleModemCountThres.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnLoadBalBasicRuleModemCountThres.setStatus("current")


class _RdnLoadBalanceUpstreamModemCount_Type(Unsigned32):
    """Custom type rdnLoadBalanceUpstreamModemCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RdnLoadBalanceUpstreamModemCount_Type.__name__ = "Unsigned32"
_RdnLoadBalanceUpstreamModemCount_Object = MibScalar
rdnLoadBalanceUpstreamModemCount = _RdnLoadBalanceUpstreamModemCount_Object(
    (1, 3, 6, 1, 4, 1, 4981, 8, 2, 1),
    _RdnLoadBalanceUpstreamModemCount_Type()
)
rdnLoadBalanceUpstreamModemCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnLoadBalanceUpstreamModemCount.setStatus("current")
if mibBuilder.loadTexts:
    rdnLoadBalanceUpstreamModemCount.setUnits("Load-Balance Group ID [0-255]")


class _RdnLoadBalanceDnstreamModemCount_Type(Unsigned32):
    """Custom type rdnLoadBalanceDnstreamModemCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RdnLoadBalanceDnstreamModemCount_Type.__name__ = "Unsigned32"
_RdnLoadBalanceDnstreamModemCount_Object = MibScalar
rdnLoadBalanceDnstreamModemCount = _RdnLoadBalanceDnstreamModemCount_Object(
    (1, 3, 6, 1, 4, 1, 4981, 8, 2, 2),
    _RdnLoadBalanceDnstreamModemCount_Type()
)
rdnLoadBalanceDnstreamModemCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnLoadBalanceDnstreamModemCount.setStatus("current")
if mibBuilder.loadTexts:
    rdnLoadBalanceDnstreamModemCount.setUnits("Load-Balance Group ID [0-255]")


class _RdnLoadBalGroupInterval_Type(Unsigned32):
    """Custom type rdnLoadBalGroupInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 480),
    )


_RdnLoadBalGroupInterval_Type.__name__ = "Unsigned32"
_RdnLoadBalGroupInterval_Object = MibScalar
rdnLoadBalGroupInterval = _RdnLoadBalGroupInterval_Object(
    (1, 3, 6, 1, 4, 1, 4981, 8, 3),
    _RdnLoadBalGroupInterval_Type()
)
rdnLoadBalGroupInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnLoadBalGroupInterval.setStatus("current")
if mibBuilder.loadTexts:
    rdnLoadBalGroupInterval.setUnits("minutes")

# Managed Objects groups

rdnLoadBalOperations = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4981, 8, 2)
)
rdnLoadBalOperations.setObjects(
      *(("RDN-DLB-MIB", "rdnLoadBalanceUpstreamModemCount"),
        ("RDN-DLB-MIB", "rdnLoadBalanceDnstreamModemCount"))
)
if mibBuilder.loadTexts:
    rdnLoadBalOperations.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RDN-DLB-MIB",
    **{"rdnLoadBalance": rdnLoadBalance,
       "rdnLoadBalBasicRuleTable": rdnLoadBalBasicRuleTable,
       "rdnLoadBalBasicRuleEntry": rdnLoadBalBasicRuleEntry,
       "rdnLoadBalBasicRuleId": rdnLoadBalBasicRuleId,
       "rdnLoadBalBasicRuleEnable": rdnLoadBalBasicRuleEnable,
       "rdnLoadBalBasicRuleMinThres": rdnLoadBalBasicRuleMinThres,
       "rdnLoadBalBasicRuleDeltaThres": rdnLoadBalBasicRuleDeltaThres,
       "rdnLoadBalBasicRuleStopThres": rdnLoadBalBasicRuleStopThres,
       "rdnLoadBalBasicRuleRowStatus": rdnLoadBalBasicRuleRowStatus,
       "rdnLoadBalBasicRuleModemCountThres": rdnLoadBalBasicRuleModemCountThres,
       "rdnLoadBalOperations": rdnLoadBalOperations,
       "rdnLoadBalanceUpstreamModemCount": rdnLoadBalanceUpstreamModemCount,
       "rdnLoadBalanceDnstreamModemCount": rdnLoadBalanceDnstreamModemCount,
       "rdnLoadBalGroupInterval": rdnLoadBalGroupInterval}
)
