# SNMP MIB module (HH3C-IP-ADDRESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-IP-ADDRESS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:35 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cIpAddrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 67)
)
hh3cIpAddrMIB.setRevisions(
        ("2005-11-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cIpAddressObjects_ObjectIdentity = ObjectIdentity
hh3cIpAddressObjects = _Hh3cIpAddressObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 67, 1)
)
_Hh3cIpAddressConfig_ObjectIdentity = ObjectIdentity
hh3cIpAddressConfig = _Hh3cIpAddressConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 67, 1, 1)
)
_Hh3cIpAddrSetTable_Object = MibTable
hh3cIpAddrSetTable = _Hh3cIpAddrSetTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 67, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cIpAddrSetTable.setStatus("current")
_Hh3cIpAddrSetEntry_Object = MibTableRow
hh3cIpAddrSetEntry = _Hh3cIpAddrSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 67, 1, 1, 1, 1)
)
hh3cIpAddrSetEntry.setIndexNames(
    (0, "HH3C-IP-ADDRESS-MIB", "hh3cIpAddrSetIfIndex"),
    (0, "HH3C-IP-ADDRESS-MIB", "hh3cIpAddrSetAddrType"),
    (0, "HH3C-IP-ADDRESS-MIB", "hh3cIpAddrSetAddr"),
)
if mibBuilder.loadTexts:
    hh3cIpAddrSetEntry.setStatus("current")


class _Hh3cIpAddrSetIfIndex_Type(Integer32):
    """Custom type hh3cIpAddrSetIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cIpAddrSetIfIndex_Type.__name__ = "Integer32"
_Hh3cIpAddrSetIfIndex_Object = MibTableColumn
hh3cIpAddrSetIfIndex = _Hh3cIpAddrSetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 67, 1, 1, 1, 1, 1),
    _Hh3cIpAddrSetIfIndex_Type()
)
hh3cIpAddrSetIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIpAddrSetIfIndex.setStatus("current")
_Hh3cIpAddrSetAddrType_Type = InetAddressType
_Hh3cIpAddrSetAddrType_Object = MibTableColumn
hh3cIpAddrSetAddrType = _Hh3cIpAddrSetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 67, 1, 1, 1, 1, 2),
    _Hh3cIpAddrSetAddrType_Type()
)
hh3cIpAddrSetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIpAddrSetAddrType.setStatus("current")
_Hh3cIpAddrSetAddr_Type = InetAddress
_Hh3cIpAddrSetAddr_Object = MibTableColumn
hh3cIpAddrSetAddr = _Hh3cIpAddrSetAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 67, 1, 1, 1, 1, 3),
    _Hh3cIpAddrSetAddr_Type()
)
hh3cIpAddrSetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIpAddrSetAddr.setStatus("current")
_Hh3cIpAddrSetMask_Type = IpAddress
_Hh3cIpAddrSetMask_Object = MibTableColumn
hh3cIpAddrSetMask = _Hh3cIpAddrSetMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 67, 1, 1, 1, 1, 4),
    _Hh3cIpAddrSetMask_Type()
)
hh3cIpAddrSetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIpAddrSetMask.setStatus("current")


class _Hh3cIpAddrSetSourceType_Type(Integer32):
    """Custom type hh3cIpAddrSetSourceType based on Integer32"""
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


_Hh3cIpAddrSetSourceType_Type.__name__ = "Integer32"
_Hh3cIpAddrSetSourceType_Object = MibTableColumn
hh3cIpAddrSetSourceType = _Hh3cIpAddrSetSourceType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 67, 1, 1, 1, 1, 5),
    _Hh3cIpAddrSetSourceType_Type()
)
hh3cIpAddrSetSourceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIpAddrSetSourceType.setStatus("current")


class _Hh3cIpAddrSetCatalog_Type(Integer32):
    """Custom type hh3cIpAddrSetCatalog based on Integer32"""
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


_Hh3cIpAddrSetCatalog_Type.__name__ = "Integer32"
_Hh3cIpAddrSetCatalog_Object = MibTableColumn
hh3cIpAddrSetCatalog = _Hh3cIpAddrSetCatalog_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 67, 1, 1, 1, 1, 6),
    _Hh3cIpAddrSetCatalog_Type()
)
hh3cIpAddrSetCatalog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIpAddrSetCatalog.setStatus("current")
_Hh3cIpAddrSetRowStatus_Type = RowStatus
_Hh3cIpAddrSetRowStatus_Object = MibTableColumn
hh3cIpAddrSetRowStatus = _Hh3cIpAddrSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 67, 1, 1, 1, 1, 7),
    _Hh3cIpAddrSetRowStatus_Type()
)
hh3cIpAddrSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIpAddrSetRowStatus.setStatus("current")
_Hh3cIpAddrReadTable_Object = MibTable
hh3cIpAddrReadTable = _Hh3cIpAddrReadTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 67, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cIpAddrReadTable.setStatus("current")
_Hh3cIpAddrReadEntry_Object = MibTableRow
hh3cIpAddrReadEntry = _Hh3cIpAddrReadEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 67, 1, 1, 2, 1)
)
hh3cIpAddrReadEntry.setIndexNames(
    (0, "HH3C-IP-ADDRESS-MIB", "hh3cIpAddrReadIfIndex"),
    (0, "HH3C-IP-ADDRESS-MIB", "hh3cIpAddrReadAddrType"),
    (0, "HH3C-IP-ADDRESS-MIB", "hh3cIpAddrReadAddr"),
)
if mibBuilder.loadTexts:
    hh3cIpAddrReadEntry.setStatus("current")


class _Hh3cIpAddrReadIfIndex_Type(Integer32):
    """Custom type hh3cIpAddrReadIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cIpAddrReadIfIndex_Type.__name__ = "Integer32"
_Hh3cIpAddrReadIfIndex_Object = MibTableColumn
hh3cIpAddrReadIfIndex = _Hh3cIpAddrReadIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 67, 1, 1, 2, 1, 1),
    _Hh3cIpAddrReadIfIndex_Type()
)
hh3cIpAddrReadIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIpAddrReadIfIndex.setStatus("current")
_Hh3cIpAddrReadAddrType_Type = InetAddressType
_Hh3cIpAddrReadAddrType_Object = MibTableColumn
hh3cIpAddrReadAddrType = _Hh3cIpAddrReadAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 67, 1, 1, 2, 1, 2),
    _Hh3cIpAddrReadAddrType_Type()
)
hh3cIpAddrReadAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIpAddrReadAddrType.setStatus("current")
_Hh3cIpAddrReadAddr_Type = InetAddress
_Hh3cIpAddrReadAddr_Object = MibTableColumn
hh3cIpAddrReadAddr = _Hh3cIpAddrReadAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 67, 1, 1, 2, 1, 3),
    _Hh3cIpAddrReadAddr_Type()
)
hh3cIpAddrReadAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIpAddrReadAddr.setStatus("current")
_Hh3cIpAddrReadMask_Type = IpAddress
_Hh3cIpAddrReadMask_Object = MibTableColumn
hh3cIpAddrReadMask = _Hh3cIpAddrReadMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 67, 1, 1, 2, 1, 4),
    _Hh3cIpAddrReadMask_Type()
)
hh3cIpAddrReadMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpAddrReadMask.setStatus("current")


class _Hh3cIpAddrReadSourceType_Type(Integer32):
    """Custom type hh3cIpAddrReadSourceType based on Integer32"""
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


_Hh3cIpAddrReadSourceType_Type.__name__ = "Integer32"
_Hh3cIpAddrReadSourceType_Object = MibTableColumn
hh3cIpAddrReadSourceType = _Hh3cIpAddrReadSourceType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 67, 1, 1, 2, 1, 5),
    _Hh3cIpAddrReadSourceType_Type()
)
hh3cIpAddrReadSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpAddrReadSourceType.setStatus("current")


class _Hh3cIpAddrReadCatalog_Type(Integer32):
    """Custom type hh3cIpAddrReadCatalog based on Integer32"""
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


_Hh3cIpAddrReadCatalog_Type.__name__ = "Integer32"
_Hh3cIpAddrReadCatalog_Object = MibTableColumn
hh3cIpAddrReadCatalog = _Hh3cIpAddrReadCatalog_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 67, 1, 1, 2, 1, 6),
    _Hh3cIpAddrReadCatalog_Type()
)
hh3cIpAddrReadCatalog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpAddrReadCatalog.setStatus("current")
_Hh3cIpv4AddrTable_Object = MibTable
hh3cIpv4AddrTable = _Hh3cIpv4AddrTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 67, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cIpv4AddrTable.setStatus("current")
_Hh3cIpv4AddrEntry_Object = MibTableRow
hh3cIpv4AddrEntry = _Hh3cIpv4AddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 67, 1, 1, 3, 1)
)
hh3cIpv4AddrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cIpv4AddrEntry.setStatus("current")
_Hh3cIpv4AddrAddr_Type = IpAddress
_Hh3cIpv4AddrAddr_Object = MibTableColumn
hh3cIpv4AddrAddr = _Hh3cIpv4AddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 67, 1, 1, 3, 1, 1),
    _Hh3cIpv4AddrAddr_Type()
)
hh3cIpv4AddrAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIpv4AddrAddr.setStatus("current")
_Hh3cIpv4AddrMask_Type = IpAddress
_Hh3cIpv4AddrMask_Object = MibTableColumn
hh3cIpv4AddrMask = _Hh3cIpv4AddrMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 67, 1, 1, 3, 1, 2),
    _Hh3cIpv4AddrMask_Type()
)
hh3cIpv4AddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIpv4AddrMask.setStatus("current")
_Hh3cIpv4AddrRowStatus_Type = RowStatus
_Hh3cIpv4AddrRowStatus_Object = MibTableColumn
hh3cIpv4AddrRowStatus = _Hh3cIpv4AddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 67, 1, 1, 3, 1, 3),
    _Hh3cIpv4AddrRowStatus_Type()
)
hh3cIpv4AddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIpv4AddrRowStatus.setStatus("current")
_Hh3cIpAddrNotify_ObjectIdentity = ObjectIdentity
hh3cIpAddrNotify = _Hh3cIpAddrNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 67, 2)
)
_Hh3cIpAddrNotifyScalarObjects_ObjectIdentity = ObjectIdentity
hh3cIpAddrNotifyScalarObjects = _Hh3cIpAddrNotifyScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 67, 2, 1)
)


class _Hh3cIpAddrNotifyIfIndex_Type(Integer32):
    """Custom type hh3cIpAddrNotifyIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cIpAddrNotifyIfIndex_Type.__name__ = "Integer32"
_Hh3cIpAddrNotifyIfIndex_Object = MibScalar
hh3cIpAddrNotifyIfIndex = _Hh3cIpAddrNotifyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 67, 2, 1, 1),
    _Hh3cIpAddrNotifyIfIndex_Type()
)
hh3cIpAddrNotifyIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cIpAddrNotifyIfIndex.setStatus("current")
_Hh3cIpAddrOldIpAddress_Type = InetAddress
_Hh3cIpAddrOldIpAddress_Object = MibScalar
hh3cIpAddrOldIpAddress = _Hh3cIpAddrOldIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 67, 2, 1, 2),
    _Hh3cIpAddrOldIpAddress_Type()
)
hh3cIpAddrOldIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cIpAddrOldIpAddress.setStatus("current")
_Hh3cIpAddrNewIpAddress_Type = InetAddress
_Hh3cIpAddrNewIpAddress_Object = MibScalar
hh3cIpAddrNewIpAddress = _Hh3cIpAddrNewIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 67, 2, 1, 3),
    _Hh3cIpAddrNewIpAddress_Type()
)
hh3cIpAddrNewIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cIpAddrNewIpAddress.setStatus("current")
_Hh3cIpAddrNotifyObjects_ObjectIdentity = ObjectIdentity
hh3cIpAddrNotifyObjects = _Hh3cIpAddrNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 67, 2, 2)
)
_Hh3cIpAddrNotifyObjectsPrefix_ObjectIdentity = ObjectIdentity
hh3cIpAddrNotifyObjectsPrefix = _Hh3cIpAddrNotifyObjectsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 67, 2, 2, 0)
)

# Managed Objects groups


# Notification objects

hh3cIpAddressChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 67, 2, 2, 0, 1)
)
hh3cIpAddressChangeNotify.setObjects(
      *(("HH3C-IP-ADDRESS-MIB", "hh3cIpAddrNotifyIfIndex"),
        ("HH3C-IP-ADDRESS-MIB", "hh3cIpAddrOldIpAddress"),
        ("HH3C-IP-ADDRESS-MIB", "hh3cIpAddrNewIpAddress"))
)
if mibBuilder.loadTexts:
    hh3cIpAddressChangeNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-IP-ADDRESS-MIB",
    **{"hh3cIpAddrMIB": hh3cIpAddrMIB,
       "hh3cIpAddressObjects": hh3cIpAddressObjects,
       "hh3cIpAddressConfig": hh3cIpAddressConfig,
       "hh3cIpAddrSetTable": hh3cIpAddrSetTable,
       "hh3cIpAddrSetEntry": hh3cIpAddrSetEntry,
       "hh3cIpAddrSetIfIndex": hh3cIpAddrSetIfIndex,
       "hh3cIpAddrSetAddrType": hh3cIpAddrSetAddrType,
       "hh3cIpAddrSetAddr": hh3cIpAddrSetAddr,
       "hh3cIpAddrSetMask": hh3cIpAddrSetMask,
       "hh3cIpAddrSetSourceType": hh3cIpAddrSetSourceType,
       "hh3cIpAddrSetCatalog": hh3cIpAddrSetCatalog,
       "hh3cIpAddrSetRowStatus": hh3cIpAddrSetRowStatus,
       "hh3cIpAddrReadTable": hh3cIpAddrReadTable,
       "hh3cIpAddrReadEntry": hh3cIpAddrReadEntry,
       "hh3cIpAddrReadIfIndex": hh3cIpAddrReadIfIndex,
       "hh3cIpAddrReadAddrType": hh3cIpAddrReadAddrType,
       "hh3cIpAddrReadAddr": hh3cIpAddrReadAddr,
       "hh3cIpAddrReadMask": hh3cIpAddrReadMask,
       "hh3cIpAddrReadSourceType": hh3cIpAddrReadSourceType,
       "hh3cIpAddrReadCatalog": hh3cIpAddrReadCatalog,
       "hh3cIpv4AddrTable": hh3cIpv4AddrTable,
       "hh3cIpv4AddrEntry": hh3cIpv4AddrEntry,
       "hh3cIpv4AddrAddr": hh3cIpv4AddrAddr,
       "hh3cIpv4AddrMask": hh3cIpv4AddrMask,
       "hh3cIpv4AddrRowStatus": hh3cIpv4AddrRowStatus,
       "hh3cIpAddrNotify": hh3cIpAddrNotify,
       "hh3cIpAddrNotifyScalarObjects": hh3cIpAddrNotifyScalarObjects,
       "hh3cIpAddrNotifyIfIndex": hh3cIpAddrNotifyIfIndex,
       "hh3cIpAddrOldIpAddress": hh3cIpAddrOldIpAddress,
       "hh3cIpAddrNewIpAddress": hh3cIpAddrNewIpAddress,
       "hh3cIpAddrNotifyObjects": hh3cIpAddrNotifyObjects,
       "hh3cIpAddrNotifyObjectsPrefix": hh3cIpAddrNotifyObjectsPrefix,
       "hh3cIpAddressChangeNotify": hh3cIpAddressChangeNotify}
)
