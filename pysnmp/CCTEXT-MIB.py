# SNMP MIB module (CCTEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CCTEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:53 2024
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

(cctExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "cctExt")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

apCctExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 29, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApCctTable_Object = MibTable
apCctTable = _ApCctTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 29, 2)
)
if mibBuilder.loadTexts:
    apCctTable.setStatus("current")
_ApCctEntry_Object = MibTableRow
apCctEntry = _ApCctEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 29, 2, 1)
)
apCctEntry.setIndexNames(
    (0, "CCTEXT-MIB", "apCctIfIndex"),
)
if mibBuilder.loadTexts:
    apCctEntry.setStatus("current")
_ApCctIfIndex_Type = Integer32
_ApCctIfIndex_Object = MibTableColumn
apCctIfIndex = _ApCctIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 29, 2, 1, 1),
    _ApCctIfIndex_Type()
)
apCctIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCctIfIndex.setStatus("current")


class _ApCctName_Type(DisplayString):
    """Custom type apCctName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ApCctName_Type.__name__ = "DisplayString"
_ApCctName_Object = MibTableColumn
apCctName = _ApCctName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 29, 2, 1, 2),
    _ApCctName_Type()
)
apCctName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCctName.setStatus("current")


class _ApCctDescription_Type(DisplayString):
    """Custom type apCctDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApCctDescription_Type.__name__ = "DisplayString"
_ApCctDescription_Object = MibTableColumn
apCctDescription = _ApCctDescription_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 29, 2, 1, 3),
    _ApCctDescription_Type()
)
apCctDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCctDescription.setStatus("current")


class _ApCctIfType_Type(Integer32):
    """Custom type apCctIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              18,
              22,
              23,
              30,
              32,
              81,
              82,
              108,
              1000,
              1001)
        )
    )
    namedValues = NamedValues(
        *(("console", 22),
          ("ds0", 81),
          ("ds0Bundle", 82),
          ("ds1", 18),
          ("ds3", 30),
          ("ethernet", 6),
          ("frameRelay", 32),
          ("ppp", 23),
          ("pppMultilink", 108),
          ("tunnel", 1000),
          ("vlan", 1001))
    )


_ApCctIfType_Type.__name__ = "Integer32"
_ApCctIfType_Object = MibTableColumn
apCctIfType = _ApCctIfType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 29, 2, 1, 4),
    _ApCctIfType_Type()
)
apCctIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCctIfType.setStatus("current")


class _ApCctState_Type(Integer32):
    """Custom type apCctState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active-ipDisabled", 1),
          ("active-ipEnabled", 3),
          ("down-ipDisabled", 0),
          ("down-ipEnabled", 2))
    )


_ApCctState_Type.__name__ = "Integer32"
_ApCctState_Object = MibTableColumn
apCctState = _ApCctState_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 29, 2, 1, 5),
    _ApCctState_Type()
)
apCctState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCctState.setStatus("current")
_ApCctLinkCount_Type = Integer32
_ApCctLinkCount_Object = MibTableColumn
apCctLinkCount = _ApCctLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 29, 2, 1, 6),
    _ApCctLinkCount_Type()
)
apCctLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCctLinkCount.setStatus("current")


class _ApCctAclIndex_Type(Integer32):
    """Custom type apCctAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ApCctAclIndex_Type.__name__ = "Integer32"
_ApCctAclIndex_Object = MibTableColumn
apCctAclIndex = _ApCctAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 29, 2, 1, 7),
    _ApCctAclIndex_Type()
)
apCctAclIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCctAclIndex.setStatus("current")


class _ApCctL2Redundancy_Type(Integer32):
    """Custom type apCctL2Redundancy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ApCctL2Redundancy_Type.__name__ = "Integer32"
_ApCctL2Redundancy_Object = MibTableColumn
apCctL2Redundancy = _ApCctL2Redundancy_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 29, 2, 1, 8),
    _ApCctL2Redundancy_Type()
)
apCctL2Redundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCctL2Redundancy.setStatus("current")


class _ApCctIrdpUseLimitedBcast_Type(TruthValue):
    """Custom type apCctIrdpUseLimitedBcast based on TruthValue"""


_ApCctIrdpUseLimitedBcast_Object = MibTableColumn
apCctIrdpUseLimitedBcast = _ApCctIrdpUseLimitedBcast_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 29, 2, 1, 9),
    _ApCctIrdpUseLimitedBcast_Type()
)
apCctIrdpUseLimitedBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCctIrdpUseLimitedBcast.setStatus("current")


class _ApCctIrdpMaxInterval_Type(Integer32):
    """Custom type apCctIrdpMaxInterval based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1800),
    )


_ApCctIrdpMaxInterval_Type.__name__ = "Integer32"
_ApCctIrdpMaxInterval_Object = MibTableColumn
apCctIrdpMaxInterval = _ApCctIrdpMaxInterval_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 29, 2, 1, 10),
    _ApCctIrdpMaxInterval_Type()
)
apCctIrdpMaxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCctIrdpMaxInterval.setStatus("current")


class _ApCctIrdpMinInterval_Type(Integer32):
    """Custom type apCctIrdpMinInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_ApCctIrdpMinInterval_Type.__name__ = "Integer32"
_ApCctIrdpMinInterval_Object = MibTableColumn
apCctIrdpMinInterval = _ApCctIrdpMinInterval_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 29, 2, 1, 11),
    _ApCctIrdpMinInterval_Type()
)
apCctIrdpMinInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCctIrdpMinInterval.setStatus("current")


class _ApCctIrdpLifetime_Type(Integer32):
    """Custom type apCctIrdpLifetime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9000),
    )


_ApCctIrdpLifetime_Type.__name__ = "Integer32"
_ApCctIrdpLifetime_Object = MibTableColumn
apCctIrdpLifetime = _ApCctIrdpLifetime_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 29, 2, 1, 12),
    _ApCctIrdpLifetime_Type()
)
apCctIrdpLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCctIrdpLifetime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CCTEXT-MIB",
    **{"apCctExtMib": apCctExtMib,
       "apCctTable": apCctTable,
       "apCctEntry": apCctEntry,
       "apCctIfIndex": apCctIfIndex,
       "apCctName": apCctName,
       "apCctDescription": apCctDescription,
       "apCctIfType": apCctIfType,
       "apCctState": apCctState,
       "apCctLinkCount": apCctLinkCount,
       "apCctAclIndex": apCctAclIndex,
       "apCctL2Redundancy": apCctL2Redundancy,
       "apCctIrdpUseLimitedBcast": apCctIrdpUseLimitedBcast,
       "apCctIrdpMaxInterval": apCctIrdpMaxInterval,
       "apCctIrdpMinInterval": apCctIrdpMinInterval,
       "apCctIrdpLifetime": apCctIrdpLifetime}
)
