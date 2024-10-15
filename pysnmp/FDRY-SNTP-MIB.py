# SNMP MIB module (FDRY-SNTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FDRY-SNTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:46 2024
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

(fdrySntp,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "fdrySntp")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fdrySntpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 7, 1)
)
fdrySntpMIB.setRevisions(
        ("2010-06-02 00:00",
         "2008-02-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FdrySntpServer_ObjectIdentity = ObjectIdentity
fdrySntpServer = _FdrySntpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 7, 1, 1)
)
_FdrySntpServerTable_Object = MibTable
fdrySntpServerTable = _FdrySntpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fdrySntpServerTable.setStatus("current")
_FdrySntpServerEntry_Object = MibTableRow
fdrySntpServerEntry = _FdrySntpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 7, 1, 1, 1, 1)
)
fdrySntpServerEntry.setIndexNames(
    (0, "FDRY-SNTP-MIB", "fdrySntpServerIndex"),
)
if mibBuilder.loadTexts:
    fdrySntpServerEntry.setStatus("current")
_FdrySntpServerIndex_Type = Unsigned32
_FdrySntpServerIndex_Object = MibTableColumn
fdrySntpServerIndex = _FdrySntpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 7, 1, 1, 1, 1, 1),
    _FdrySntpServerIndex_Type()
)
fdrySntpServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdrySntpServerIndex.setStatus("current")


class _FdrySntpServerAddrType_Type(InetAddressType):
    """Custom type fdrySntpServerAddrType based on InetAddressType"""


_FdrySntpServerAddrType_Object = MibTableColumn
fdrySntpServerAddrType = _FdrySntpServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 7, 1, 1, 1, 1, 2),
    _FdrySntpServerAddrType_Type()
)
fdrySntpServerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdrySntpServerAddrType.setStatus("current")
_FdrySntpServerAddr_Type = InetAddress
_FdrySntpServerAddr_Object = MibTableColumn
fdrySntpServerAddr = _FdrySntpServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 7, 1, 1, 1, 1, 3),
    _FdrySntpServerAddr_Type()
)
fdrySntpServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdrySntpServerAddr.setStatus("current")


class _FdrySntpServerVersion_Type(Integer32):
    """Custom type fdrySntpServerVersion based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_FdrySntpServerVersion_Type.__name__ = "Integer32"
_FdrySntpServerVersion_Object = MibTableColumn
fdrySntpServerVersion = _FdrySntpServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 7, 1, 1, 1, 1, 4),
    _FdrySntpServerVersion_Type()
)
fdrySntpServerVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdrySntpServerVersion.setStatus("current")
_FdrySntpServerRowStatus_Type = RowStatus
_FdrySntpServerRowStatus_Object = MibTableColumn
fdrySntpServerRowStatus = _FdrySntpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 7, 1, 1, 1, 1, 5),
    _FdrySntpServerRowStatus_Type()
)
fdrySntpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdrySntpServerRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FDRY-SNTP-MIB",
    **{"fdrySntpMIB": fdrySntpMIB,
       "fdrySntpServer": fdrySntpServer,
       "fdrySntpServerTable": fdrySntpServerTable,
       "fdrySntpServerEntry": fdrySntpServerEntry,
       "fdrySntpServerIndex": fdrySntpServerIndex,
       "fdrySntpServerAddrType": fdrySntpServerAddrType,
       "fdrySntpServerAddr": fdrySntpServerAddr,
       "fdrySntpServerVersion": fdrySntpServerVersion,
       "fdrySntpServerRowStatus": fdrySntpServerRowStatus}
)
