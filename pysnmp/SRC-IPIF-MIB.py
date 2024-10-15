# SNMP MIB module (SRC-IPIF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SRC-IPIF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:38 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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

swSrcIpIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 81)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwSrcIpIfCtrl_ObjectIdentity = ObjectIdentity
swSrcIpIfCtrl = _SwSrcIpIfCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 81, 1)
)
_SwSrcIpIfInfo_ObjectIdentity = ObjectIdentity
swSrcIpIfInfo = _SwSrcIpIfInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 81, 2)
)
_SwSrcIpIfMgmt_ObjectIdentity = ObjectIdentity
swSrcIpIfMgmt = _SwSrcIpIfMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 81, 3)
)
_SwSrcIpIfTable_Object = MibTable
swSrcIpIfTable = _SwSrcIpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 81, 3, 1)
)
if mibBuilder.loadTexts:
    swSrcIpIfTable.setStatus("current")
_SwSrcIpIfEntry_Object = MibTableRow
swSrcIpIfEntry = _SwSrcIpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 81, 3, 1, 1)
)
swSrcIpIfEntry.setIndexNames(
    (0, "SRC-IPIF-MIB", "swSrcIpIfType"),
)
if mibBuilder.loadTexts:
    swSrcIpIfEntry.setStatus("current")


class _SwSrcIpIfType_Type(Integer32):
    """Custom type swSrcIpIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("syslog", 2),
          ("trap", 1))
    )


_SwSrcIpIfType_Type.__name__ = "Integer32"
_SwSrcIpIfType_Object = MibTableColumn
swSrcIpIfType = _SwSrcIpIfType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 81, 3, 1, 1, 1),
    _SwSrcIpIfType_Type()
)
swSrcIpIfType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swSrcIpIfType.setStatus("current")
_SwSrcIpIfRowStatus_Type = RowStatus
_SwSrcIpIfRowStatus_Object = MibTableColumn
swSrcIpIfRowStatus = _SwSrcIpIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 81, 3, 1, 1, 2),
    _SwSrcIpIfRowStatus_Type()
)
swSrcIpIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSrcIpIfRowStatus.setStatus("current")


class _SwSrcIpIfName_Type(DisplayString):
    """Custom type swSrcIpIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SwSrcIpIfName_Type.__name__ = "DisplayString"
_SwSrcIpIfName_Object = MibTableColumn
swSrcIpIfName = _SwSrcIpIfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 81, 3, 1, 1, 3),
    _SwSrcIpIfName_Type()
)
swSrcIpIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSrcIpIfName.setStatus("current")
_SwSrcIpIfIPAddr_Type = IpAddress
_SwSrcIpIfIPAddr_Object = MibTableColumn
swSrcIpIfIPAddr = _SwSrcIpIfIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 81, 3, 1, 1, 4),
    _SwSrcIpIfIPAddr_Type()
)
swSrcIpIfIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSrcIpIfIPAddr.setStatus("current")
_SwSrcIpIfIPv6Addr_Type = Ipv6Address
_SwSrcIpIfIPv6Addr_Object = MibTableColumn
swSrcIpIfIPv6Addr = _SwSrcIpIfIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 81, 3, 1, 1, 5),
    _SwSrcIpIfIPv6Addr_Type()
)
swSrcIpIfIPv6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSrcIpIfIPv6Addr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SRC-IPIF-MIB",
    **{"swSrcIpIfMIB": swSrcIpIfMIB,
       "swSrcIpIfCtrl": swSrcIpIfCtrl,
       "swSrcIpIfInfo": swSrcIpIfInfo,
       "swSrcIpIfMgmt": swSrcIpIfMgmt,
       "swSrcIpIfTable": swSrcIpIfTable,
       "swSrcIpIfEntry": swSrcIpIfEntry,
       "swSrcIpIfType": swSrcIpIfType,
       "swSrcIpIfRowStatus": swSrcIpIfRowStatus,
       "swSrcIpIfName": swSrcIpIfName,
       "swSrcIpIfIPAddr": swSrcIpIfIPAddr,
       "swSrcIpIfIPv6Addr": swSrcIpIfIPv6Addr}
)
