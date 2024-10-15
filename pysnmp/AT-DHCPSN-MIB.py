# SNMP MIB module (AT-DHCPSN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-DHCPSN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:01 2024
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

(modules,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "modules")

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

atDhcpsn = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537)
)
atDhcpsn.setRevisions(
        ("2010-09-07 00:00",
         "2010-06-14 04:45",
         "2010-02-09 01:30",
         "2009-12-10 01:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtDhcpsnEvents_ObjectIdentity = ObjectIdentity
atDhcpsnEvents = _AtDhcpsnEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 0)
)
_AtDhcpsnVariablesTable_Object = MibTable
atDhcpsnVariablesTable = _AtDhcpsnVariablesTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1)
)
if mibBuilder.loadTexts:
    atDhcpsnVariablesTable.setStatus("current")
_AtDhcpsnVariablesEntry_Object = MibTableRow
atDhcpsnVariablesEntry = _AtDhcpsnVariablesEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1, 1)
)
atDhcpsnVariablesEntry.setIndexNames(
    (0, "AT-DHCPSN-MIB", "atDhcpsnIfIndex"),
)
if mibBuilder.loadTexts:
    atDhcpsnVariablesEntry.setStatus("current")


class _AtDhcpsnIfIndex_Type(Integer32):
    """Custom type atDhcpsnIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AtDhcpsnIfIndex_Type.__name__ = "Integer32"
_AtDhcpsnIfIndex_Object = MibTableColumn
atDhcpsnIfIndex = _AtDhcpsnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1, 1, 1),
    _AtDhcpsnIfIndex_Type()
)
atDhcpsnIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atDhcpsnIfIndex.setStatus("current")
_AtDhcpsnVid_Type = Integer32
_AtDhcpsnVid_Object = MibTableColumn
atDhcpsnVid = _AtDhcpsnVid_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1, 1, 2),
    _AtDhcpsnVid_Type()
)
atDhcpsnVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atDhcpsnVid.setStatus("current")
_AtDhcpsnSmac_Type = DisplayString
_AtDhcpsnSmac_Object = MibTableColumn
atDhcpsnSmac = _AtDhcpsnSmac_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1, 1, 3),
    _AtDhcpsnSmac_Type()
)
atDhcpsnSmac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atDhcpsnSmac.setStatus("current")


class _AtDhcpsnOpcode_Type(Integer32):
    """Custom type atDhcpsnOpcode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootpReply", 2),
          ("bootpRequest", 1))
    )


_AtDhcpsnOpcode_Type.__name__ = "Integer32"
_AtDhcpsnOpcode_Object = MibTableColumn
atDhcpsnOpcode = _AtDhcpsnOpcode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1, 1, 4),
    _AtDhcpsnOpcode_Type()
)
atDhcpsnOpcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atDhcpsnOpcode.setStatus("current")
_AtDhcpsnCiaddr_Type = IpAddress
_AtDhcpsnCiaddr_Object = MibTableColumn
atDhcpsnCiaddr = _AtDhcpsnCiaddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1, 1, 5),
    _AtDhcpsnCiaddr_Type()
)
atDhcpsnCiaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atDhcpsnCiaddr.setStatus("current")
_AtDhcpsnYiaddr_Type = IpAddress
_AtDhcpsnYiaddr_Object = MibTableColumn
atDhcpsnYiaddr = _AtDhcpsnYiaddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1, 1, 6),
    _AtDhcpsnYiaddr_Type()
)
atDhcpsnYiaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atDhcpsnYiaddr.setStatus("current")
_AtDhcpsnGiaddr_Type = IpAddress
_AtDhcpsnGiaddr_Object = MibTableColumn
atDhcpsnGiaddr = _AtDhcpsnGiaddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1, 1, 7),
    _AtDhcpsnGiaddr_Type()
)
atDhcpsnGiaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atDhcpsnGiaddr.setStatus("current")
_AtDhcpsnSiaddr_Type = IpAddress
_AtDhcpsnSiaddr_Object = MibTableColumn
atDhcpsnSiaddr = _AtDhcpsnSiaddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1, 1, 8),
    _AtDhcpsnSiaddr_Type()
)
atDhcpsnSiaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atDhcpsnSiaddr.setStatus("current")
_AtDhcpsnChaddr_Type = DisplayString
_AtDhcpsnChaddr_Object = MibTableColumn
atDhcpsnChaddr = _AtDhcpsnChaddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1, 1, 9),
    _AtDhcpsnChaddr_Type()
)
atDhcpsnChaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atDhcpsnChaddr.setStatus("current")


class _AtDhcpsnVioType_Type(Integer32):
    """Custom type atDhcpsnVioType based on Integer32"""
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
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("dbAddErr", 13),
          ("invalidBootp", 1),
          ("invalidDhcpAck", 2),
          ("invalidDhcpRelDec", 3),
          ("invalidIp", 4),
          ("maxBindExceeded", 5),
          ("opt82InsertErr", 6),
          ("opt82RxInvalid", 7),
          ("opt82RxUntrusted", 8),
          ("opt82TxUntrusted", 9),
          ("replyRxUntrusted", 10),
          ("srcMacChaddrMismatch", 11),
          ("staticEntryExisted", 12))
    )


_AtDhcpsnVioType_Type.__name__ = "Integer32"
_AtDhcpsnVioType_Object = MibTableColumn
atDhcpsnVioType = _AtDhcpsnVioType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1, 1, 10),
    _AtDhcpsnVioType_Type()
)
atDhcpsnVioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atDhcpsnVioType.setStatus("current")
_AtArpsecVariablesTable_Object = MibTable
atArpsecVariablesTable = _AtArpsecVariablesTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 2)
)
if mibBuilder.loadTexts:
    atArpsecVariablesTable.setStatus("current")
_AtArpsecVariablesEntry_Object = MibTableRow
atArpsecVariablesEntry = _AtArpsecVariablesEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 2, 1)
)
atArpsecVariablesEntry.setIndexNames(
    (0, "AT-DHCPSN-MIB", "atArpsecIfIndex"),
)
if mibBuilder.loadTexts:
    atArpsecVariablesEntry.setStatus("current")


class _AtArpsecIfIndex_Type(Integer32):
    """Custom type atArpsecIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AtArpsecIfIndex_Type.__name__ = "Integer32"
_AtArpsecIfIndex_Object = MibTableColumn
atArpsecIfIndex = _AtArpsecIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 2, 1, 1),
    _AtArpsecIfIndex_Type()
)
atArpsecIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atArpsecIfIndex.setStatus("current")
_AtArpsecClientIP_Type = IpAddress
_AtArpsecClientIP_Object = MibTableColumn
atArpsecClientIP = _AtArpsecClientIP_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 2, 1, 2),
    _AtArpsecClientIP_Type()
)
atArpsecClientIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atArpsecClientIP.setStatus("current")
_AtArpsecSrcMac_Type = DisplayString
_AtArpsecSrcMac_Object = MibTableColumn
atArpsecSrcMac = _AtArpsecSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 2, 1, 3),
    _AtArpsecSrcMac_Type()
)
atArpsecSrcMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atArpsecSrcMac.setStatus("current")
_AtArpsecVid_Type = Integer32
_AtArpsecVid_Object = MibTableColumn
atArpsecVid = _AtArpsecVid_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 2, 1, 4),
    _AtArpsecVid_Type()
)
atArpsecVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atArpsecVid.setStatus("current")


class _AtArpsecVioType_Type(Integer32):
    """Custom type atArpsecVioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("badPort", 3),
          ("badVLAN", 2),
          ("srcIpNotAllocated", 4),
          ("srcIpNotFound", 1))
    )


_AtArpsecVioType_Type.__name__ = "Integer32"
_AtArpsecVioType_Object = MibTableColumn
atArpsecVioType = _AtArpsecVioType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 2, 1, 5),
    _AtArpsecVioType_Type()
)
atArpsecVioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atArpsecVioType.setStatus("current")

# Managed Objects groups


# Notification objects

atDhcpsnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 0, 1)
)
atDhcpsnTrap.setObjects(
      *(("AT-DHCPSN-MIB", "atDhcpsnIfIndex"),
        ("AT-DHCPSN-MIB", "atDhcpsnVid"),
        ("AT-DHCPSN-MIB", "atDhcpsnSmac"),
        ("AT-DHCPSN-MIB", "atDhcpsnOpcode"),
        ("AT-DHCPSN-MIB", "atDhcpsnCiaddr"),
        ("AT-DHCPSN-MIB", "atDhcpsnYiaddr"),
        ("AT-DHCPSN-MIB", "atDhcpsnGiaddr"),
        ("AT-DHCPSN-MIB", "atDhcpsnSiaddr"),
        ("AT-DHCPSN-MIB", "atDhcpsnChaddr"),
        ("AT-DHCPSN-MIB", "atDhcpsnVioType"))
)
if mibBuilder.loadTexts:
    atDhcpsnTrap.setStatus(
        "current"
    )

atArpsecTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 0, 2)
)
atArpsecTrap.setObjects(
      *(("AT-DHCPSN-MIB", "atArpsecIfIndex"),
        ("AT-DHCPSN-MIB", "atArpsecClientIP"),
        ("AT-DHCPSN-MIB", "atArpsecSrcMac"),
        ("AT-DHCPSN-MIB", "atArpsecVid"),
        ("AT-DHCPSN-MIB", "atArpsecVioType"))
)
if mibBuilder.loadTexts:
    atArpsecTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-DHCPSN-MIB",
    **{"atDhcpsn": atDhcpsn,
       "atDhcpsnEvents": atDhcpsnEvents,
       "atDhcpsnTrap": atDhcpsnTrap,
       "atArpsecTrap": atArpsecTrap,
       "atDhcpsnVariablesTable": atDhcpsnVariablesTable,
       "atDhcpsnVariablesEntry": atDhcpsnVariablesEntry,
       "atDhcpsnIfIndex": atDhcpsnIfIndex,
       "atDhcpsnVid": atDhcpsnVid,
       "atDhcpsnSmac": atDhcpsnSmac,
       "atDhcpsnOpcode": atDhcpsnOpcode,
       "atDhcpsnCiaddr": atDhcpsnCiaddr,
       "atDhcpsnYiaddr": atDhcpsnYiaddr,
       "atDhcpsnGiaddr": atDhcpsnGiaddr,
       "atDhcpsnSiaddr": atDhcpsnSiaddr,
       "atDhcpsnChaddr": atDhcpsnChaddr,
       "atDhcpsnVioType": atDhcpsnVioType,
       "atArpsecVariablesTable": atArpsecVariablesTable,
       "atArpsecVariablesEntry": atArpsecVariablesEntry,
       "atArpsecIfIndex": atArpsecIfIndex,
       "atArpsecClientIP": atArpsecClientIP,
       "atArpsecSrcMac": atArpsecSrcMac,
       "atArpsecVid": atArpsecVid,
       "atArpsecVioType": atArpsecVioType}
)
