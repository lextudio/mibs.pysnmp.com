# SNMP MIB module (JUNIPER-IF-ACCOUNTING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-IF-ACCOUNTING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:06 2024
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(JnxCosFcIdentifier,) = mibBuilder.importSymbols(
    "JUNIPER-COS-MIB",
    "JnxCosFcIdentifier")

(ifJnx,) = mibBuilder.importSymbols(
    "JUNIPER-IF-MIB",
    "ifJnx")

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

jnxIfAccountingStats = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 10)
)
jnxIfAccountingStats.setRevisions(
        ("2013-05-15 12:23",
         "2013-12-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxIfFcAccountStatTable_Object = MibTable
jnxIfFcAccountStatTable = _JnxIfFcAccountStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 10, 1)
)
if mibBuilder.loadTexts:
    jnxIfFcAccountStatTable.setStatus("current")
_JnxIfFcAccountStatEntry_Object = MibTableRow
jnxIfFcAccountStatEntry = _JnxIfFcAccountStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 10, 1, 1)
)
jnxIfFcAccountStatEntry.setIndexNames(
    (0, "JUNIPER-IF-ACCOUNTING-MIB", "jnxIfFcIfIndex"),
    (0, "JUNIPER-IF-ACCOUNTING-MIB", "jnxIfFcFcIndex"),
    (0, "JUNIPER-IF-ACCOUNTING-MIB", "jnxIfFcProtocol"),
)
if mibBuilder.loadTexts:
    jnxIfFcAccountStatEntry.setStatus("current")
_JnxIfFcIfIndex_Type = InterfaceIndex
_JnxIfFcIfIndex_Object = MibTableColumn
jnxIfFcIfIndex = _JnxIfFcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 10, 1, 1, 1),
    _JnxIfFcIfIndex_Type()
)
jnxIfFcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfFcIfIndex.setStatus("current")
_JnxIfFcFcIndex_Type = JnxCosFcIdentifier
_JnxIfFcFcIndex_Object = MibTableColumn
jnxIfFcFcIndex = _JnxIfFcFcIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 10, 1, 1, 2),
    _JnxIfFcFcIndex_Type()
)
jnxIfFcFcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfFcFcIndex.setStatus("current")


class _JnxIfFcProtocol_Type(Integer32):
    """Custom type jnxIfFcProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("ipv4", 2),
          ("ipv6", 3),
          ("layer2", 5),
          ("mpls", 4),
          ("other", 6))
    )


_JnxIfFcProtocol_Type.__name__ = "Integer32"
_JnxIfFcProtocol_Object = MibTableColumn
jnxIfFcProtocol = _JnxIfFcProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 10, 1, 1, 3),
    _JnxIfFcProtocol_Type()
)
jnxIfFcProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxIfFcProtocol.setStatus("current")
_JnxIfFcHCInUcastPkts_Type = Counter64
_JnxIfFcHCInUcastPkts_Object = MibTableColumn
jnxIfFcHCInUcastPkts = _JnxIfFcHCInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 10, 1, 1, 4),
    _JnxIfFcHCInUcastPkts_Type()
)
jnxIfFcHCInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfFcHCInUcastPkts.setStatus("current")
_JnxIfFcHCInUcastOctets_Type = Counter64
_JnxIfFcHCInUcastOctets_Object = MibTableColumn
jnxIfFcHCInUcastOctets = _JnxIfFcHCInUcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 10, 1, 1, 5),
    _JnxIfFcHCInUcastOctets_Type()
)
jnxIfFcHCInUcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfFcHCInUcastOctets.setStatus("current")
_JnxIfFcHCOutUcastPkts_Type = Counter64
_JnxIfFcHCOutUcastPkts_Object = MibTableColumn
jnxIfFcHCOutUcastPkts = _JnxIfFcHCOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 10, 1, 1, 6),
    _JnxIfFcHCOutUcastPkts_Type()
)
jnxIfFcHCOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfFcHCOutUcastPkts.setStatus("current")
_JnxIfFcHCOutUcastOctets_Type = Counter64
_JnxIfFcHCOutUcastOctets_Object = MibTableColumn
jnxIfFcHCOutUcastOctets = _JnxIfFcHCOutUcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 10, 1, 1, 7),
    _JnxIfFcHCOutUcastOctets_Type()
)
jnxIfFcHCOutUcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfFcHCOutUcastOctets.setStatus("current")
_JnxIfFcHCInMcastPkts_Type = Counter64
_JnxIfFcHCInMcastPkts_Object = MibTableColumn
jnxIfFcHCInMcastPkts = _JnxIfFcHCInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 10, 1, 1, 8),
    _JnxIfFcHCInMcastPkts_Type()
)
jnxIfFcHCInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfFcHCInMcastPkts.setStatus("current")
_JnxIfFcHCInMcastOctets_Type = Counter64
_JnxIfFcHCInMcastOctets_Object = MibTableColumn
jnxIfFcHCInMcastOctets = _JnxIfFcHCInMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 10, 1, 1, 9),
    _JnxIfFcHCInMcastOctets_Type()
)
jnxIfFcHCInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfFcHCInMcastOctets.setStatus("current")
_JnxIfFcHCOutMcastPkts_Type = Counter64
_JnxIfFcHCOutMcastPkts_Object = MibTableColumn
jnxIfFcHCOutMcastPkts = _JnxIfFcHCOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 10, 1, 1, 10),
    _JnxIfFcHCOutMcastPkts_Type()
)
jnxIfFcHCOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfFcHCOutMcastPkts.setStatus("current")
_JnxIfFcHCOutMcastOctets_Type = Counter64
_JnxIfFcHCOutMcastOctets_Object = MibTableColumn
jnxIfFcHCOutMcastOctets = _JnxIfFcHCOutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 10, 1, 1, 11),
    _JnxIfFcHCOutMcastOctets_Type()
)
jnxIfFcHCOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfFcHCOutMcastOctets.setStatus("current")
_JnxIfFcInlineAccountingStatTable_Object = MibTable
jnxIfFcInlineAccountingStatTable = _JnxIfFcInlineAccountingStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 10, 2)
)
if mibBuilder.loadTexts:
    jnxIfFcInlineAccountingStatTable.setStatus("current")
_JnxIfFcInlineAccountingStatEntry_Object = MibTableRow
jnxIfFcInlineAccountingStatEntry = _JnxIfFcInlineAccountingStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 10, 2, 1)
)
jnxIfFcInlineAccountingStatEntry.setIndexNames(
    (0, "JUNIPER-IF-ACCOUNTING-MIB", "jnxIfFcIfIndex"),
    (0, "JUNIPER-IF-ACCOUNTING-MIB", "jnxIfFcFcIndex"),
    (0, "JUNIPER-IF-ACCOUNTING-MIB", "jnxIfFcProtocol"),
)
if mibBuilder.loadTexts:
    jnxIfFcInlineAccountingStatEntry.setStatus("current")
_JnxIfFcInlineHCInPkts_Type = Counter64
_JnxIfFcInlineHCInPkts_Object = MibTableColumn
jnxIfFcInlineHCInPkts = _JnxIfFcInlineHCInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 10, 2, 1, 1),
    _JnxIfFcInlineHCInPkts_Type()
)
jnxIfFcInlineHCInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfFcInlineHCInPkts.setStatus("current")
_JnxIfFcInlineHCInPktsSecRate_Type = CounterBasedGauge64
_JnxIfFcInlineHCInPktsSecRate_Object = MibTableColumn
jnxIfFcInlineHCInPktsSecRate = _JnxIfFcInlineHCInPktsSecRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 10, 2, 1, 2),
    _JnxIfFcInlineHCInPktsSecRate_Type()
)
jnxIfFcInlineHCInPktsSecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfFcInlineHCInPktsSecRate.setStatus("current")
_JnxIfFcInlineHCInOctets_Type = Counter64
_JnxIfFcInlineHCInOctets_Object = MibTableColumn
jnxIfFcInlineHCInOctets = _JnxIfFcInlineHCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 10, 2, 1, 3),
    _JnxIfFcInlineHCInOctets_Type()
)
jnxIfFcInlineHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfFcInlineHCInOctets.setStatus("current")
_JnxIfFcInlineHCInOctetsSecRate_Type = CounterBasedGauge64
_JnxIfFcInlineHCInOctetsSecRate_Object = MibTableColumn
jnxIfFcInlineHCInOctetsSecRate = _JnxIfFcInlineHCInOctetsSecRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 10, 2, 1, 4),
    _JnxIfFcInlineHCInOctetsSecRate_Type()
)
jnxIfFcInlineHCInOctetsSecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfFcInlineHCInOctetsSecRate.setStatus("current")
_JnxIfFcInlineHCOutPkts_Type = Counter64
_JnxIfFcInlineHCOutPkts_Object = MibTableColumn
jnxIfFcInlineHCOutPkts = _JnxIfFcInlineHCOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 10, 2, 1, 5),
    _JnxIfFcInlineHCOutPkts_Type()
)
jnxIfFcInlineHCOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfFcInlineHCOutPkts.setStatus("current")
_JnxIfFcInlineHCOutPktsSecRate_Type = CounterBasedGauge64
_JnxIfFcInlineHCOutPktsSecRate_Object = MibTableColumn
jnxIfFcInlineHCOutPktsSecRate = _JnxIfFcInlineHCOutPktsSecRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 10, 2, 1, 6),
    _JnxIfFcInlineHCOutPktsSecRate_Type()
)
jnxIfFcInlineHCOutPktsSecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfFcInlineHCOutPktsSecRate.setStatus("current")
_JnxIfFcInlineHCOutOctets_Type = Counter64
_JnxIfFcInlineHCOutOctets_Object = MibTableColumn
jnxIfFcInlineHCOutOctets = _JnxIfFcInlineHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 10, 2, 1, 7),
    _JnxIfFcInlineHCOutOctets_Type()
)
jnxIfFcInlineHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfFcInlineHCOutOctets.setStatus("current")
_JnxIfFcInlineHCOutOctetsSecRate_Type = CounterBasedGauge64
_JnxIfFcInlineHCOutOctetsSecRate_Object = MibTableColumn
jnxIfFcInlineHCOutOctetsSecRate = _JnxIfFcInlineHCOutOctetsSecRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 3, 10, 2, 1, 8),
    _JnxIfFcInlineHCOutOctetsSecRate_Type()
)
jnxIfFcInlineHCOutOctetsSecRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxIfFcInlineHCOutOctetsSecRate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-IF-ACCOUNTING-MIB",
    **{"jnxIfAccountingStats": jnxIfAccountingStats,
       "jnxIfFcAccountStatTable": jnxIfFcAccountStatTable,
       "jnxIfFcAccountStatEntry": jnxIfFcAccountStatEntry,
       "jnxIfFcIfIndex": jnxIfFcIfIndex,
       "jnxIfFcFcIndex": jnxIfFcFcIndex,
       "jnxIfFcProtocol": jnxIfFcProtocol,
       "jnxIfFcHCInUcastPkts": jnxIfFcHCInUcastPkts,
       "jnxIfFcHCInUcastOctets": jnxIfFcHCInUcastOctets,
       "jnxIfFcHCOutUcastPkts": jnxIfFcHCOutUcastPkts,
       "jnxIfFcHCOutUcastOctets": jnxIfFcHCOutUcastOctets,
       "jnxIfFcHCInMcastPkts": jnxIfFcHCInMcastPkts,
       "jnxIfFcHCInMcastOctets": jnxIfFcHCInMcastOctets,
       "jnxIfFcHCOutMcastPkts": jnxIfFcHCOutMcastPkts,
       "jnxIfFcHCOutMcastOctets": jnxIfFcHCOutMcastOctets,
       "jnxIfFcInlineAccountingStatTable": jnxIfFcInlineAccountingStatTable,
       "jnxIfFcInlineAccountingStatEntry": jnxIfFcInlineAccountingStatEntry,
       "jnxIfFcInlineHCInPkts": jnxIfFcInlineHCInPkts,
       "jnxIfFcInlineHCInPktsSecRate": jnxIfFcInlineHCInPktsSecRate,
       "jnxIfFcInlineHCInOctets": jnxIfFcInlineHCInOctets,
       "jnxIfFcInlineHCInOctetsSecRate": jnxIfFcInlineHCInOctetsSecRate,
       "jnxIfFcInlineHCOutPkts": jnxIfFcInlineHCOutPkts,
       "jnxIfFcInlineHCOutPktsSecRate": jnxIfFcInlineHCOutPktsSecRate,
       "jnxIfFcInlineHCOutOctets": jnxIfFcInlineHCOutOctets,
       "jnxIfFcInlineHCOutOctetsSecRate": jnxIfFcInlineHCOutOctetsSecRate}
)
