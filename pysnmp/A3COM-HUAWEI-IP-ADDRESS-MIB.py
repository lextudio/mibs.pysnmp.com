# SNMP MIB module (A3COM-HUAWEI-IP-ADDRESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-IP-ADDRESS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:28:08 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

h3cIpAddrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 67)
)
h3cIpAddrMIB.setRevisions(
        ("2005-11-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cIpAddressObjects_ObjectIdentity = ObjectIdentity
h3cIpAddressObjects = _H3cIpAddressObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 67, 1)
)
_H3cIpAddressConfig_ObjectIdentity = ObjectIdentity
h3cIpAddressConfig = _H3cIpAddressConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 67, 1, 1)
)
_H3cIpAddrSetTable_Object = MibTable
h3cIpAddrSetTable = _H3cIpAddrSetTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 67, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h3cIpAddrSetTable.setStatus("current")
_H3cIpAddrSetEntry_Object = MibTableRow
h3cIpAddrSetEntry = _H3cIpAddrSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 67, 1, 1, 1, 1)
)
h3cIpAddrSetEntry.setIndexNames(
    (0, "A3COM-HUAWEI-IP-ADDRESS-MIB", "h3cIpAddrSetIfIndex"),
    (0, "A3COM-HUAWEI-IP-ADDRESS-MIB", "h3cIpAddrSetAddrType"),
    (0, "A3COM-HUAWEI-IP-ADDRESS-MIB", "h3cIpAddrSetAddr"),
)
if mibBuilder.loadTexts:
    h3cIpAddrSetEntry.setStatus("current")


class _H3cIpAddrSetIfIndex_Type(Integer32):
    """Custom type h3cIpAddrSetIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cIpAddrSetIfIndex_Type.__name__ = "Integer32"
_H3cIpAddrSetIfIndex_Object = MibTableColumn
h3cIpAddrSetIfIndex = _H3cIpAddrSetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 67, 1, 1, 1, 1, 1),
    _H3cIpAddrSetIfIndex_Type()
)
h3cIpAddrSetIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIpAddrSetIfIndex.setStatus("current")
_H3cIpAddrSetAddrType_Type = InetAddressType
_H3cIpAddrSetAddrType_Object = MibTableColumn
h3cIpAddrSetAddrType = _H3cIpAddrSetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 67, 1, 1, 1, 1, 2),
    _H3cIpAddrSetAddrType_Type()
)
h3cIpAddrSetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIpAddrSetAddrType.setStatus("current")
_H3cIpAddrSetAddr_Type = InetAddress
_H3cIpAddrSetAddr_Object = MibTableColumn
h3cIpAddrSetAddr = _H3cIpAddrSetAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 67, 1, 1, 1, 1, 3),
    _H3cIpAddrSetAddr_Type()
)
h3cIpAddrSetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIpAddrSetAddr.setStatus("current")
_H3cIpAddrSetMask_Type = IpAddress
_H3cIpAddrSetMask_Object = MibTableColumn
h3cIpAddrSetMask = _H3cIpAddrSetMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 67, 1, 1, 1, 1, 4),
    _H3cIpAddrSetMask_Type()
)
h3cIpAddrSetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIpAddrSetMask.setStatus("current")


class _H3cIpAddrSetSourceType_Type(Integer32):
    """Custom type h3cIpAddrSetSourceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("assignedIp", 1)
    )


_H3cIpAddrSetSourceType_Type.__name__ = "Integer32"
_H3cIpAddrSetSourceType_Object = MibTableColumn
h3cIpAddrSetSourceType = _H3cIpAddrSetSourceType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 67, 1, 1, 1, 1, 5),
    _H3cIpAddrSetSourceType_Type()
)
h3cIpAddrSetSourceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIpAddrSetSourceType.setStatus("current")


class _H3cIpAddrSetCatalog_Type(Integer32):
    """Custom type h3cIpAddrSetCatalog based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("sub", 2))
    )


_H3cIpAddrSetCatalog_Type.__name__ = "Integer32"
_H3cIpAddrSetCatalog_Object = MibTableColumn
h3cIpAddrSetCatalog = _H3cIpAddrSetCatalog_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 67, 1, 1, 1, 1, 6),
    _H3cIpAddrSetCatalog_Type()
)
h3cIpAddrSetCatalog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIpAddrSetCatalog.setStatus("current")
_H3cIpAddrSetRowStatus_Type = RowStatus
_H3cIpAddrSetRowStatus_Object = MibTableColumn
h3cIpAddrSetRowStatus = _H3cIpAddrSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 67, 1, 1, 1, 1, 7),
    _H3cIpAddrSetRowStatus_Type()
)
h3cIpAddrSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIpAddrSetRowStatus.setStatus("current")
_H3cIpAddrReadTable_Object = MibTable
h3cIpAddrReadTable = _H3cIpAddrReadTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 67, 1, 1, 2)
)
if mibBuilder.loadTexts:
    h3cIpAddrReadTable.setStatus("current")
_H3cIpAddrReadEntry_Object = MibTableRow
h3cIpAddrReadEntry = _H3cIpAddrReadEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 67, 1, 1, 2, 1)
)
h3cIpAddrReadEntry.setIndexNames(
    (0, "A3COM-HUAWEI-IP-ADDRESS-MIB", "h3cIpAddrReadIfIndex"),
    (0, "A3COM-HUAWEI-IP-ADDRESS-MIB", "h3cIpAddrReadAddrType"),
    (0, "A3COM-HUAWEI-IP-ADDRESS-MIB", "h3cIpAddrReadAddr"),
)
if mibBuilder.loadTexts:
    h3cIpAddrReadEntry.setStatus("current")


class _H3cIpAddrReadIfIndex_Type(Integer32):
    """Custom type h3cIpAddrReadIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cIpAddrReadIfIndex_Type.__name__ = "Integer32"
_H3cIpAddrReadIfIndex_Object = MibTableColumn
h3cIpAddrReadIfIndex = _H3cIpAddrReadIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 67, 1, 1, 2, 1, 1),
    _H3cIpAddrReadIfIndex_Type()
)
h3cIpAddrReadIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIpAddrReadIfIndex.setStatus("current")
_H3cIpAddrReadAddrType_Type = InetAddressType
_H3cIpAddrReadAddrType_Object = MibTableColumn
h3cIpAddrReadAddrType = _H3cIpAddrReadAddrType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 67, 1, 1, 2, 1, 2),
    _H3cIpAddrReadAddrType_Type()
)
h3cIpAddrReadAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIpAddrReadAddrType.setStatus("current")
_H3cIpAddrReadAddr_Type = InetAddress
_H3cIpAddrReadAddr_Object = MibTableColumn
h3cIpAddrReadAddr = _H3cIpAddrReadAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 67, 1, 1, 2, 1, 3),
    _H3cIpAddrReadAddr_Type()
)
h3cIpAddrReadAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIpAddrReadAddr.setStatus("current")
_H3cIpAddrReadMask_Type = IpAddress
_H3cIpAddrReadMask_Object = MibTableColumn
h3cIpAddrReadMask = _H3cIpAddrReadMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 67, 1, 1, 2, 1, 4),
    _H3cIpAddrReadMask_Type()
)
h3cIpAddrReadMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIpAddrReadMask.setStatus("current")


class _H3cIpAddrReadSourceType_Type(Integer32):
    """Custom type h3cIpAddrReadSourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("assignedIp", 1),
          ("bootp", 4),
          ("cluster", 2),
          ("dhcp", 3),
          ("negotiate", 5),
          ("unnumbered", 6),
          ("vrrp", 7))
    )


_H3cIpAddrReadSourceType_Type.__name__ = "Integer32"
_H3cIpAddrReadSourceType_Object = MibTableColumn
h3cIpAddrReadSourceType = _H3cIpAddrReadSourceType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 67, 1, 1, 2, 1, 5),
    _H3cIpAddrReadSourceType_Type()
)
h3cIpAddrReadSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIpAddrReadSourceType.setStatus("current")


class _H3cIpAddrReadCatalog_Type(Integer32):
    """Custom type h3cIpAddrReadCatalog based on Integer32"""
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
        *(("cluster", 3),
          ("primary", 1),
          ("sub", 2),
          ("vrrp", 4))
    )


_H3cIpAddrReadCatalog_Type.__name__ = "Integer32"
_H3cIpAddrReadCatalog_Object = MibTableColumn
h3cIpAddrReadCatalog = _H3cIpAddrReadCatalog_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 67, 1, 1, 2, 1, 6),
    _H3cIpAddrReadCatalog_Type()
)
h3cIpAddrReadCatalog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIpAddrReadCatalog.setStatus("current")
_H3cIpv4AddrTable_Object = MibTable
h3cIpv4AddrTable = _H3cIpv4AddrTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 67, 1, 1, 3)
)
if mibBuilder.loadTexts:
    h3cIpv4AddrTable.setStatus("current")
_H3cIpv4AddrEntry_Object = MibTableRow
h3cIpv4AddrEntry = _H3cIpv4AddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 67, 1, 1, 3, 1)
)
h3cIpv4AddrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cIpv4AddrEntry.setStatus("current")
_H3cIpv4AddrAddr_Type = IpAddress
_H3cIpv4AddrAddr_Object = MibTableColumn
h3cIpv4AddrAddr = _H3cIpv4AddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 67, 1, 1, 3, 1, 1),
    _H3cIpv4AddrAddr_Type()
)
h3cIpv4AddrAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIpv4AddrAddr.setStatus("current")
_H3cIpv4AddrMask_Type = IpAddress
_H3cIpv4AddrMask_Object = MibTableColumn
h3cIpv4AddrMask = _H3cIpv4AddrMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 67, 1, 1, 3, 1, 2),
    _H3cIpv4AddrMask_Type()
)
h3cIpv4AddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIpv4AddrMask.setStatus("current")
_H3cIpv4AddrRowStatus_Type = RowStatus
_H3cIpv4AddrRowStatus_Object = MibTableColumn
h3cIpv4AddrRowStatus = _H3cIpv4AddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 67, 1, 1, 3, 1, 3),
    _H3cIpv4AddrRowStatus_Type()
)
h3cIpv4AddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIpv4AddrRowStatus.setStatus("current")
_H3cIpAddrNotify_ObjectIdentity = ObjectIdentity
h3cIpAddrNotify = _H3cIpAddrNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 67, 2)
)
_H3cIpAddrNotifyScalarObjects_ObjectIdentity = ObjectIdentity
h3cIpAddrNotifyScalarObjects = _H3cIpAddrNotifyScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 67, 2, 1)
)


class _H3cIpAddrNotifyIfIndex_Type(Integer32):
    """Custom type h3cIpAddrNotifyIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cIpAddrNotifyIfIndex_Type.__name__ = "Integer32"
_H3cIpAddrNotifyIfIndex_Object = MibScalar
h3cIpAddrNotifyIfIndex = _H3cIpAddrNotifyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 67, 2, 1, 1),
    _H3cIpAddrNotifyIfIndex_Type()
)
h3cIpAddrNotifyIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cIpAddrNotifyIfIndex.setStatus("current")
_H3cIpAddrOldIpAddress_Type = InetAddress
_H3cIpAddrOldIpAddress_Object = MibScalar
h3cIpAddrOldIpAddress = _H3cIpAddrOldIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 67, 2, 1, 2),
    _H3cIpAddrOldIpAddress_Type()
)
h3cIpAddrOldIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cIpAddrOldIpAddress.setStatus("current")
_H3cIpAddrNewIpAddress_Type = InetAddress
_H3cIpAddrNewIpAddress_Object = MibScalar
h3cIpAddrNewIpAddress = _H3cIpAddrNewIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 67, 2, 1, 3),
    _H3cIpAddrNewIpAddress_Type()
)
h3cIpAddrNewIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cIpAddrNewIpAddress.setStatus("current")
_H3cIpAddrFirstTrapTime_Type = TimeTicks
_H3cIpAddrFirstTrapTime_Object = MibScalar
h3cIpAddrFirstTrapTime = _H3cIpAddrFirstTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 67, 2, 1, 4),
    _H3cIpAddrFirstTrapTime_Type()
)
h3cIpAddrFirstTrapTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cIpAddrFirstTrapTime.setStatus("current")
_H3cIpAddrNotifyObjects_ObjectIdentity = ObjectIdentity
h3cIpAddrNotifyObjects = _H3cIpAddrNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 67, 2, 2)
)
_H3cIpAddrNotifyObjectsPrefix_ObjectIdentity = ObjectIdentity
h3cIpAddrNotifyObjectsPrefix = _H3cIpAddrNotifyObjectsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 67, 2, 2, 0)
)

# Managed Objects groups


# Notification objects

h3cIpAddressChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 67, 2, 2, 0, 1)
)
h3cIpAddressChangeNotify.setObjects(
      *(("A3COM-HUAWEI-IP-ADDRESS-MIB", "h3cIpAddrNotifyIfIndex"),
        ("A3COM-HUAWEI-IP-ADDRESS-MIB", "h3cIpAddrOldIpAddress"),
        ("A3COM-HUAWEI-IP-ADDRESS-MIB", "h3cIpAddrNewIpAddress"),
        ("A3COM-HUAWEI-IP-ADDRESS-MIB", "h3cIpAddrFirstTrapTime"))
)
if mibBuilder.loadTexts:
    h3cIpAddressChangeNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-IP-ADDRESS-MIB",
    **{"h3cIpAddrMIB": h3cIpAddrMIB,
       "h3cIpAddressObjects": h3cIpAddressObjects,
       "h3cIpAddressConfig": h3cIpAddressConfig,
       "h3cIpAddrSetTable": h3cIpAddrSetTable,
       "h3cIpAddrSetEntry": h3cIpAddrSetEntry,
       "h3cIpAddrSetIfIndex": h3cIpAddrSetIfIndex,
       "h3cIpAddrSetAddrType": h3cIpAddrSetAddrType,
       "h3cIpAddrSetAddr": h3cIpAddrSetAddr,
       "h3cIpAddrSetMask": h3cIpAddrSetMask,
       "h3cIpAddrSetSourceType": h3cIpAddrSetSourceType,
       "h3cIpAddrSetCatalog": h3cIpAddrSetCatalog,
       "h3cIpAddrSetRowStatus": h3cIpAddrSetRowStatus,
       "h3cIpAddrReadTable": h3cIpAddrReadTable,
       "h3cIpAddrReadEntry": h3cIpAddrReadEntry,
       "h3cIpAddrReadIfIndex": h3cIpAddrReadIfIndex,
       "h3cIpAddrReadAddrType": h3cIpAddrReadAddrType,
       "h3cIpAddrReadAddr": h3cIpAddrReadAddr,
       "h3cIpAddrReadMask": h3cIpAddrReadMask,
       "h3cIpAddrReadSourceType": h3cIpAddrReadSourceType,
       "h3cIpAddrReadCatalog": h3cIpAddrReadCatalog,
       "h3cIpv4AddrTable": h3cIpv4AddrTable,
       "h3cIpv4AddrEntry": h3cIpv4AddrEntry,
       "h3cIpv4AddrAddr": h3cIpv4AddrAddr,
       "h3cIpv4AddrMask": h3cIpv4AddrMask,
       "h3cIpv4AddrRowStatus": h3cIpv4AddrRowStatus,
       "h3cIpAddrNotify": h3cIpAddrNotify,
       "h3cIpAddrNotifyScalarObjects": h3cIpAddrNotifyScalarObjects,
       "h3cIpAddrNotifyIfIndex": h3cIpAddrNotifyIfIndex,
       "h3cIpAddrOldIpAddress": h3cIpAddrOldIpAddress,
       "h3cIpAddrNewIpAddress": h3cIpAddrNewIpAddress,
       "h3cIpAddrFirstTrapTime": h3cIpAddrFirstTrapTime,
       "h3cIpAddrNotifyObjects": h3cIpAddrNotifyObjects,
       "h3cIpAddrNotifyObjectsPrefix": h3cIpAddrNotifyObjectsPrefix,
       "h3cIpAddressChangeNotify": h3cIpAddressChangeNotify}
)
