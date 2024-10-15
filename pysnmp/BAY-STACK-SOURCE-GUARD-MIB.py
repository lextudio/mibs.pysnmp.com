# SNMP MIB module (BAY-STACK-SOURCE-GUARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAY-STACK-SOURCE-GUARD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:21 2024
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
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

bayStackSourceGuardMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 20)
)
bayStackSourceGuardMib.setRevisions(
        ("2008-10-30 00:00",
         "2008-03-31 00:00",
         "2007-05-07 00:00",
         "2007-03-23 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BsSourceGuardNotifications_ObjectIdentity = ObjectIdentity
bsSourceGuardNotifications = _BsSourceGuardNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 20, 0)
)
_BsSourceGuardObjects_ObjectIdentity = ObjectIdentity
bsSourceGuardObjects = _BsSourceGuardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 20, 1)
)
_BsSourceGuardConfigTable_Object = MibTable
bsSourceGuardConfigTable = _BsSourceGuardConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 1)
)
if mibBuilder.loadTexts:
    bsSourceGuardConfigTable.setStatus("current")
_BsSourceGuardConfigEntry_Object = MibTableRow
bsSourceGuardConfigEntry = _BsSourceGuardConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 1, 1)
)
bsSourceGuardConfigEntry.setIndexNames(
    (0, "BAY-STACK-SOURCE-GUARD-MIB", "bsSourceGuardConfigIfIndex"),
)
if mibBuilder.loadTexts:
    bsSourceGuardConfigEntry.setStatus("current")
_BsSourceGuardConfigIfIndex_Type = InterfaceIndex
_BsSourceGuardConfigIfIndex_Object = MibTableColumn
bsSourceGuardConfigIfIndex = _BsSourceGuardConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 1, 1, 1),
    _BsSourceGuardConfigIfIndex_Type()
)
bsSourceGuardConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsSourceGuardConfigIfIndex.setStatus("current")


class _BsSourceGuardConfigMode_Type(Integer32):
    """Custom type bsSourceGuardConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("ip", 2))
    )


_BsSourceGuardConfigMode_Type.__name__ = "Integer32"
_BsSourceGuardConfigMode_Object = MibTableColumn
bsSourceGuardConfigMode = _BsSourceGuardConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 1, 1, 2),
    _BsSourceGuardConfigMode_Type()
)
bsSourceGuardConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsSourceGuardConfigMode.setStatus("current")
_BsSourceGuardAddrTable_Object = MibTable
bsSourceGuardAddrTable = _BsSourceGuardAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 2)
)
if mibBuilder.loadTexts:
    bsSourceGuardAddrTable.setStatus("current")
_BsSourceGuardAddrEntry_Object = MibTableRow
bsSourceGuardAddrEntry = _BsSourceGuardAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 2, 1)
)
bsSourceGuardAddrEntry.setIndexNames(
    (0, "BAY-STACK-SOURCE-GUARD-MIB", "bsSourceGuardAddrIndex"),
    (0, "BAY-STACK-SOURCE-GUARD-MIB", "bsSourceGuardAddrType"),
    (0, "BAY-STACK-SOURCE-GUARD-MIB", "bsSourceGuardAddrAddress"),
    (0, "BAY-STACK-SOURCE-GUARD-MIB", "bsSourceGuardAddrMACAddr"),
)
if mibBuilder.loadTexts:
    bsSourceGuardAddrEntry.setStatus("current")
_BsSourceGuardAddrIndex_Type = InterfaceIndex
_BsSourceGuardAddrIndex_Object = MibTableColumn
bsSourceGuardAddrIndex = _BsSourceGuardAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 2, 1, 1),
    _BsSourceGuardAddrIndex_Type()
)
bsSourceGuardAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsSourceGuardAddrIndex.setStatus("current")
_BsSourceGuardAddrType_Type = InetAddressType
_BsSourceGuardAddrType_Object = MibTableColumn
bsSourceGuardAddrType = _BsSourceGuardAddrType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 2, 1, 2),
    _BsSourceGuardAddrType_Type()
)
bsSourceGuardAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsSourceGuardAddrType.setStatus("current")
_BsSourceGuardAddrAddress_Type = InetAddress
_BsSourceGuardAddrAddress_Object = MibTableColumn
bsSourceGuardAddrAddress = _BsSourceGuardAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 2, 1, 3),
    _BsSourceGuardAddrAddress_Type()
)
bsSourceGuardAddrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsSourceGuardAddrAddress.setStatus("current")
_BsSourceGuardAddrMACAddr_Type = MacAddress
_BsSourceGuardAddrMACAddr_Object = MibTableColumn
bsSourceGuardAddrMACAddr = _BsSourceGuardAddrMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 2, 1, 4),
    _BsSourceGuardAddrMACAddr_Type()
)
bsSourceGuardAddrMACAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsSourceGuardAddrMACAddr.setStatus("current")


class _BsSourceGuardAddrSource_Type(Integer32):
    """Custom type bsSourceGuardAddrSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("dhcpSnooping", 1)
    )


_BsSourceGuardAddrSource_Type.__name__ = "Integer32"
_BsSourceGuardAddrSource_Object = MibTableColumn
bsSourceGuardAddrSource = _BsSourceGuardAddrSource_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 2, 1, 5),
    _BsSourceGuardAddrSource_Type()
)
bsSourceGuardAddrSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsSourceGuardAddrSource.setStatus("current")
_BsSourceGuardStatsTable_Object = MibTable
bsSourceGuardStatsTable = _BsSourceGuardStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 3)
)
if mibBuilder.loadTexts:
    bsSourceGuardStatsTable.setStatus("current")
_BsSourceGuardStatsEntry_Object = MibTableRow
bsSourceGuardStatsEntry = _BsSourceGuardStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 3, 1)
)
bsSourceGuardStatsEntry.setIndexNames(
    (0, "BAY-STACK-SOURCE-GUARD-MIB", "bsSourceGuardStatsIfIndex"),
)
if mibBuilder.loadTexts:
    bsSourceGuardStatsEntry.setStatus("current")
_BsSourceGuardStatsIfIndex_Type = InterfaceIndex
_BsSourceGuardStatsIfIndex_Object = MibTableColumn
bsSourceGuardStatsIfIndex = _BsSourceGuardStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 3, 1, 1),
    _BsSourceGuardStatsIfIndex_Type()
)
bsSourceGuardStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsSourceGuardStatsIfIndex.setStatus("current")
_BsSourceGuardStatsDroppedPackets_Type = Counter32
_BsSourceGuardStatsDroppedPackets_Object = MibTableColumn
bsSourceGuardStatsDroppedPackets = _BsSourceGuardStatsDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 20, 1, 3, 1, 2),
    _BsSourceGuardStatsDroppedPackets_Type()
)
bsSourceGuardStatsDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsSourceGuardStatsDroppedPackets.setStatus("current")

# Managed Objects groups


# Notification objects

bsSourceGuardReachedMaxIpEntries = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 20, 0, 1)
)
bsSourceGuardReachedMaxIpEntries.setObjects(
    ("BAY-STACK-SOURCE-GUARD-MIB", "bsSourceGuardConfigMode")
)
if mibBuilder.loadTexts:
    bsSourceGuardReachedMaxIpEntries.setStatus(
        "current"
    )

bsSourceGuardCannotEnablePort = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 20, 0, 2)
)
bsSourceGuardCannotEnablePort.setObjects(
    ("BAY-STACK-SOURCE-GUARD-MIB", "bsSourceGuardConfigMode")
)
if mibBuilder.loadTexts:
    bsSourceGuardCannotEnablePort.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAY-STACK-SOURCE-GUARD-MIB",
    **{"bayStackSourceGuardMib": bayStackSourceGuardMib,
       "bsSourceGuardNotifications": bsSourceGuardNotifications,
       "bsSourceGuardReachedMaxIpEntries": bsSourceGuardReachedMaxIpEntries,
       "bsSourceGuardCannotEnablePort": bsSourceGuardCannotEnablePort,
       "bsSourceGuardObjects": bsSourceGuardObjects,
       "bsSourceGuardConfigTable": bsSourceGuardConfigTable,
       "bsSourceGuardConfigEntry": bsSourceGuardConfigEntry,
       "bsSourceGuardConfigIfIndex": bsSourceGuardConfigIfIndex,
       "bsSourceGuardConfigMode": bsSourceGuardConfigMode,
       "bsSourceGuardAddrTable": bsSourceGuardAddrTable,
       "bsSourceGuardAddrEntry": bsSourceGuardAddrEntry,
       "bsSourceGuardAddrIndex": bsSourceGuardAddrIndex,
       "bsSourceGuardAddrType": bsSourceGuardAddrType,
       "bsSourceGuardAddrAddress": bsSourceGuardAddrAddress,
       "bsSourceGuardAddrMACAddr": bsSourceGuardAddrMACAddr,
       "bsSourceGuardAddrSource": bsSourceGuardAddrSource,
       "bsSourceGuardStatsTable": bsSourceGuardStatsTable,
       "bsSourceGuardStatsEntry": bsSourceGuardStatsEntry,
       "bsSourceGuardStatsIfIndex": bsSourceGuardStatsIfIndex,
       "bsSourceGuardStatsDroppedPackets": bsSourceGuardStatsDroppedPackets}
)
