# SNMP MIB module (JUNIPER-FIREWALL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-FIREWALL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:03 2024
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

(jnxMibs,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs")

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

jnxFirewalls = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 5)
)
jnxFirewalls.setRevisions(
        ("2016-01-23 15:53",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxFirewallsTable_Object = MibTable
jnxFirewallsTable = _JnxFirewallsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 5, 1)
)
if mibBuilder.loadTexts:
    jnxFirewallsTable.setStatus("deprecated")
_JnxFirewallsEntry_Object = MibTableRow
jnxFirewallsEntry = _JnxFirewallsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 5, 1, 1)
)
jnxFirewallsEntry.setIndexNames(
    (0, "JUNIPER-FIREWALL-MIB", "jnxFWFilter"),
    (0, "JUNIPER-FIREWALL-MIB", "jnxFWCounter"),
)
if mibBuilder.loadTexts:
    jnxFirewallsEntry.setStatus("current")


class _JnxFWFilter_Type(DisplayString):
    """Custom type jnxFWFilter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_JnxFWFilter_Type.__name__ = "DisplayString"
_JnxFWFilter_Object = MibTableColumn
jnxFWFilter = _JnxFWFilter_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 5, 1, 1, 1),
    _JnxFWFilter_Type()
)
jnxFWFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFWFilter.setStatus("current")


class _JnxFWCounter_Type(DisplayString):
    """Custom type jnxFWCounter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_JnxFWCounter_Type.__name__ = "DisplayString"
_JnxFWCounter_Object = MibTableColumn
jnxFWCounter = _JnxFWCounter_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 5, 1, 1, 2),
    _JnxFWCounter_Type()
)
jnxFWCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFWCounter.setStatus("current")


class _JnxFWType_Type(Integer32):
    """Custom type jnxFWType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("counter", 2),
          ("hpolagg", 4),
          ("hpolpre", 5),
          ("other", 1),
          ("policer", 3))
    )


_JnxFWType_Type.__name__ = "Integer32"
_JnxFWType_Object = MibTableColumn
jnxFWType = _JnxFWType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 5, 1, 1, 3),
    _JnxFWType_Type()
)
jnxFWType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFWType.setStatus("current")
_JnxFWPackets_Type = Counter64
_JnxFWPackets_Object = MibTableColumn
jnxFWPackets = _JnxFWPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 5, 1, 1, 4),
    _JnxFWPackets_Type()
)
jnxFWPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFWPackets.setStatus("current")
_JnxFWBytes_Type = Counter64
_JnxFWBytes_Object = MibTableColumn
jnxFWBytes = _JnxFWBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 5, 1, 1, 5),
    _JnxFWBytes_Type()
)
jnxFWBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFWBytes.setStatus("current")
_JnxFirewallCounterTable_Object = MibTable
jnxFirewallCounterTable = _JnxFirewallCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 5, 2)
)
if mibBuilder.loadTexts:
    jnxFirewallCounterTable.setStatus("current")
_JnxFirewallCounterEntry_Object = MibTableRow
jnxFirewallCounterEntry = _JnxFirewallCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 5, 2, 1)
)
jnxFirewallCounterEntry.setIndexNames(
    (0, "JUNIPER-FIREWALL-MIB", "jnxFWCounterFilterName"),
    (0, "JUNIPER-FIREWALL-MIB", "jnxFWCounterName"),
    (0, "JUNIPER-FIREWALL-MIB", "jnxFWCounterType"),
)
if mibBuilder.loadTexts:
    jnxFirewallCounterEntry.setStatus("current")


class _JnxFWCounterFilterName_Type(DisplayString):
    """Custom type jnxFWCounterFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_JnxFWCounterFilterName_Type.__name__ = "DisplayString"
_JnxFWCounterFilterName_Object = MibTableColumn
jnxFWCounterFilterName = _JnxFWCounterFilterName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 5, 2, 1, 1),
    _JnxFWCounterFilterName_Type()
)
jnxFWCounterFilterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxFWCounterFilterName.setStatus("current")


class _JnxFWCounterName_Type(DisplayString):
    """Custom type jnxFWCounterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_JnxFWCounterName_Type.__name__ = "DisplayString"
_JnxFWCounterName_Object = MibTableColumn
jnxFWCounterName = _JnxFWCounterName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 5, 2, 1, 2),
    _JnxFWCounterName_Type()
)
jnxFWCounterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxFWCounterName.setStatus("current")


class _JnxFWCounterType_Type(Integer32):
    """Custom type jnxFWCounterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("counter", 2),
          ("hpolagg", 4),
          ("hpolpre", 5),
          ("other", 1),
          ("policer", 3))
    )


_JnxFWCounterType_Type.__name__ = "Integer32"
_JnxFWCounterType_Object = MibTableColumn
jnxFWCounterType = _JnxFWCounterType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 5, 2, 1, 3),
    _JnxFWCounterType_Type()
)
jnxFWCounterType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxFWCounterType.setStatus("current")
_JnxFWCounterPacketCount_Type = Counter64
_JnxFWCounterPacketCount_Object = MibTableColumn
jnxFWCounterPacketCount = _JnxFWCounterPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 5, 2, 1, 4),
    _JnxFWCounterPacketCount_Type()
)
jnxFWCounterPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFWCounterPacketCount.setStatus("current")
_JnxFWCounterByteCount_Type = Counter64
_JnxFWCounterByteCount_Object = MibTableColumn
jnxFWCounterByteCount = _JnxFWCounterByteCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 5, 2, 1, 5),
    _JnxFWCounterByteCount_Type()
)
jnxFWCounterByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFWCounterByteCount.setStatus("current")


class _JnxFWCounterDisplayFilterName_Type(DisplayString):
    """Custom type jnxFWCounterDisplayFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_JnxFWCounterDisplayFilterName_Type.__name__ = "DisplayString"
_JnxFWCounterDisplayFilterName_Object = MibTableColumn
jnxFWCounterDisplayFilterName = _JnxFWCounterDisplayFilterName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 5, 2, 1, 6),
    _JnxFWCounterDisplayFilterName_Type()
)
jnxFWCounterDisplayFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFWCounterDisplayFilterName.setStatus("current")


class _JnxFWCounterDisplayName_Type(DisplayString):
    """Custom type jnxFWCounterDisplayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_JnxFWCounterDisplayName_Type.__name__ = "DisplayString"
_JnxFWCounterDisplayName_Object = MibTableColumn
jnxFWCounterDisplayName = _JnxFWCounterDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 5, 2, 1, 7),
    _JnxFWCounterDisplayName_Type()
)
jnxFWCounterDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFWCounterDisplayName.setStatus("current")


class _JnxFWCounterDisplayType_Type(Integer32):
    """Custom type jnxFWCounterDisplayType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("counter", 2),
          ("hpolagg", 4),
          ("hpolpre", 5),
          ("other", 1),
          ("policer", 3))
    )


_JnxFWCounterDisplayType_Type.__name__ = "Integer32"
_JnxFWCounterDisplayType_Object = MibTableColumn
jnxFWCounterDisplayType = _JnxFWCounterDisplayType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 5, 2, 1, 8),
    _JnxFWCounterDisplayType_Type()
)
jnxFWCounterDisplayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFWCounterDisplayType.setStatus("current")
_JnxFWCntrXTable_Object = MibTable
jnxFWCntrXTable = _JnxFWCntrXTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 5, 3)
)
if mibBuilder.loadTexts:
    jnxFWCntrXTable.setStatus("current")
_JnxFWCntrXEntry_Object = MibTableRow
jnxFWCntrXEntry = _JnxFWCntrXEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 5, 3, 1)
)
if mibBuilder.loadTexts:
    jnxFWCntrXEntry.setStatus("current")
_JnxFWCntrPolicerOfferedPktCount_Type = Counter64
_JnxFWCntrPolicerOfferedPktCount_Object = MibTableColumn
jnxFWCntrPolicerOfferedPktCount = _JnxFWCntrPolicerOfferedPktCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 5, 3, 1, 1),
    _JnxFWCntrPolicerOfferedPktCount_Type()
)
jnxFWCntrPolicerOfferedPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFWCntrPolicerOfferedPktCount.setStatus("current")
_JnxFWCntrPolicerOfferedByteCount_Type = Counter64
_JnxFWCntrPolicerOfferedByteCount_Object = MibTableColumn
jnxFWCntrPolicerOfferedByteCount = _JnxFWCntrPolicerOfferedByteCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 5, 3, 1, 2),
    _JnxFWCntrPolicerOfferedByteCount_Type()
)
jnxFWCntrPolicerOfferedByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFWCntrPolicerOfferedByteCount.setStatus("current")
_JnxFWCntrPolicerOutSpecPktCount_Type = Counter64
_JnxFWCntrPolicerOutSpecPktCount_Object = MibTableColumn
jnxFWCntrPolicerOutSpecPktCount = _JnxFWCntrPolicerOutSpecPktCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 5, 3, 1, 3),
    _JnxFWCntrPolicerOutSpecPktCount_Type()
)
jnxFWCntrPolicerOutSpecPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFWCntrPolicerOutSpecPktCount.setStatus("current")
_JnxFWCntrPolicerOutSpecByteCount_Type = Counter64
_JnxFWCntrPolicerOutSpecByteCount_Object = MibTableColumn
jnxFWCntrPolicerOutSpecByteCount = _JnxFWCntrPolicerOutSpecByteCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 5, 3, 1, 4),
    _JnxFWCntrPolicerOutSpecByteCount_Type()
)
jnxFWCntrPolicerOutSpecByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFWCntrPolicerOutSpecByteCount.setStatus("current")
_JnxFWCntrPolicerTxPktCount_Type = Counter64
_JnxFWCntrPolicerTxPktCount_Object = MibTableColumn
jnxFWCntrPolicerTxPktCount = _JnxFWCntrPolicerTxPktCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 5, 3, 1, 5),
    _JnxFWCntrPolicerTxPktCount_Type()
)
jnxFWCntrPolicerTxPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFWCntrPolicerTxPktCount.setStatus("current")
_JnxFWCntrPolicerTxByteCount_Type = Counter64
_JnxFWCntrPolicerTxByteCount_Object = MibTableColumn
jnxFWCntrPolicerTxByteCount = _JnxFWCntrPolicerTxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 5, 3, 1, 6),
    _JnxFWCntrPolicerTxByteCount_Type()
)
jnxFWCntrPolicerTxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFWCntrPolicerTxByteCount.setStatus("current")
jnxFirewallCounterEntry.registerAugmentions(
    ("JUNIPER-FIREWALL-MIB",
     "jnxFWCntrXEntry")
)
jnxFWCntrXEntry.setIndexNames(*jnxFirewallCounterEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-FIREWALL-MIB",
    **{"jnxFirewalls": jnxFirewalls,
       "jnxFirewallsTable": jnxFirewallsTable,
       "jnxFirewallsEntry": jnxFirewallsEntry,
       "jnxFWFilter": jnxFWFilter,
       "jnxFWCounter": jnxFWCounter,
       "jnxFWType": jnxFWType,
       "jnxFWPackets": jnxFWPackets,
       "jnxFWBytes": jnxFWBytes,
       "jnxFirewallCounterTable": jnxFirewallCounterTable,
       "jnxFirewallCounterEntry": jnxFirewallCounterEntry,
       "jnxFWCounterFilterName": jnxFWCounterFilterName,
       "jnxFWCounterName": jnxFWCounterName,
       "jnxFWCounterType": jnxFWCounterType,
       "jnxFWCounterPacketCount": jnxFWCounterPacketCount,
       "jnxFWCounterByteCount": jnxFWCounterByteCount,
       "jnxFWCounterDisplayFilterName": jnxFWCounterDisplayFilterName,
       "jnxFWCounterDisplayName": jnxFWCounterDisplayName,
       "jnxFWCounterDisplayType": jnxFWCounterDisplayType,
       "jnxFWCntrXTable": jnxFWCntrXTable,
       "jnxFWCntrXEntry": jnxFWCntrXEntry,
       "jnxFWCntrPolicerOfferedPktCount": jnxFWCntrPolicerOfferedPktCount,
       "jnxFWCntrPolicerOfferedByteCount": jnxFWCntrPolicerOfferedByteCount,
       "jnxFWCntrPolicerOutSpecPktCount": jnxFWCntrPolicerOutSpecPktCount,
       "jnxFWCntrPolicerOutSpecByteCount": jnxFWCntrPolicerOutSpecByteCount,
       "jnxFWCntrPolicerTxPktCount": jnxFWCntrPolicerTxPktCount,
       "jnxFWCntrPolicerTxByteCount": jnxFWCntrPolicerTxByteCount}
)
