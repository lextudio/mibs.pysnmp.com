# SNMP MIB module (HPN-ICF-IP-ADDRESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-IP-ADDRESS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:35 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfIpAddrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67)
)
hpnicfIpAddrMIB.setRevisions(
        ("2005-11-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfIpAddressObjects_ObjectIdentity = ObjectIdentity
hpnicfIpAddressObjects = _HpnicfIpAddressObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1)
)
_HpnicfIpAddressConfig_ObjectIdentity = ObjectIdentity
hpnicfIpAddressConfig = _HpnicfIpAddressConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1)
)
_HpnicfIpAddrSetTable_Object = MibTable
hpnicfIpAddrSetTable = _HpnicfIpAddrSetTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfIpAddrSetTable.setStatus("current")
_HpnicfIpAddrSetEntry_Object = MibTableRow
hpnicfIpAddrSetEntry = _HpnicfIpAddrSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 1, 1)
)
hpnicfIpAddrSetEntry.setIndexNames(
    (0, "HPN-ICF-IP-ADDRESS-MIB", "hpnicfIpAddrSetIfIndex"),
    (0, "HPN-ICF-IP-ADDRESS-MIB", "hpnicfIpAddrSetAddrType"),
    (0, "HPN-ICF-IP-ADDRESS-MIB", "hpnicfIpAddrSetAddr"),
)
if mibBuilder.loadTexts:
    hpnicfIpAddrSetEntry.setStatus("current")


class _HpnicfIpAddrSetIfIndex_Type(Integer32):
    """Custom type hpnicfIpAddrSetIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfIpAddrSetIfIndex_Type.__name__ = "Integer32"
_HpnicfIpAddrSetIfIndex_Object = MibTableColumn
hpnicfIpAddrSetIfIndex = _HpnicfIpAddrSetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 1, 1, 1),
    _HpnicfIpAddrSetIfIndex_Type()
)
hpnicfIpAddrSetIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIpAddrSetIfIndex.setStatus("current")
_HpnicfIpAddrSetAddrType_Type = InetAddressType
_HpnicfIpAddrSetAddrType_Object = MibTableColumn
hpnicfIpAddrSetAddrType = _HpnicfIpAddrSetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 1, 1, 2),
    _HpnicfIpAddrSetAddrType_Type()
)
hpnicfIpAddrSetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIpAddrSetAddrType.setStatus("current")
_HpnicfIpAddrSetAddr_Type = InetAddress
_HpnicfIpAddrSetAddr_Object = MibTableColumn
hpnicfIpAddrSetAddr = _HpnicfIpAddrSetAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 1, 1, 3),
    _HpnicfIpAddrSetAddr_Type()
)
hpnicfIpAddrSetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIpAddrSetAddr.setStatus("current")
_HpnicfIpAddrSetMask_Type = IpAddress
_HpnicfIpAddrSetMask_Object = MibTableColumn
hpnicfIpAddrSetMask = _HpnicfIpAddrSetMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 1, 1, 4),
    _HpnicfIpAddrSetMask_Type()
)
hpnicfIpAddrSetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIpAddrSetMask.setStatus("current")


class _HpnicfIpAddrSetSourceType_Type(Integer32):
    """Custom type hpnicfIpAddrSetSourceType based on Integer32"""
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


_HpnicfIpAddrSetSourceType_Type.__name__ = "Integer32"
_HpnicfIpAddrSetSourceType_Object = MibTableColumn
hpnicfIpAddrSetSourceType = _HpnicfIpAddrSetSourceType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 1, 1, 5),
    _HpnicfIpAddrSetSourceType_Type()
)
hpnicfIpAddrSetSourceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIpAddrSetSourceType.setStatus("current")


class _HpnicfIpAddrSetCatalog_Type(Integer32):
    """Custom type hpnicfIpAddrSetCatalog based on Integer32"""
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


_HpnicfIpAddrSetCatalog_Type.__name__ = "Integer32"
_HpnicfIpAddrSetCatalog_Object = MibTableColumn
hpnicfIpAddrSetCatalog = _HpnicfIpAddrSetCatalog_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 1, 1, 6),
    _HpnicfIpAddrSetCatalog_Type()
)
hpnicfIpAddrSetCatalog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIpAddrSetCatalog.setStatus("current")
_HpnicfIpAddrSetRowStatus_Type = RowStatus
_HpnicfIpAddrSetRowStatus_Object = MibTableColumn
hpnicfIpAddrSetRowStatus = _HpnicfIpAddrSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 1, 1, 7),
    _HpnicfIpAddrSetRowStatus_Type()
)
hpnicfIpAddrSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIpAddrSetRowStatus.setStatus("current")
_HpnicfIpAddrReadTable_Object = MibTable
hpnicfIpAddrReadTable = _HpnicfIpAddrReadTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfIpAddrReadTable.setStatus("current")
_HpnicfIpAddrReadEntry_Object = MibTableRow
hpnicfIpAddrReadEntry = _HpnicfIpAddrReadEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 2, 1)
)
hpnicfIpAddrReadEntry.setIndexNames(
    (0, "HPN-ICF-IP-ADDRESS-MIB", "hpnicfIpAddrReadIfIndex"),
    (0, "HPN-ICF-IP-ADDRESS-MIB", "hpnicfIpAddrReadAddrType"),
    (0, "HPN-ICF-IP-ADDRESS-MIB", "hpnicfIpAddrReadAddr"),
)
if mibBuilder.loadTexts:
    hpnicfIpAddrReadEntry.setStatus("current")


class _HpnicfIpAddrReadIfIndex_Type(Integer32):
    """Custom type hpnicfIpAddrReadIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfIpAddrReadIfIndex_Type.__name__ = "Integer32"
_HpnicfIpAddrReadIfIndex_Object = MibTableColumn
hpnicfIpAddrReadIfIndex = _HpnicfIpAddrReadIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 2, 1, 1),
    _HpnicfIpAddrReadIfIndex_Type()
)
hpnicfIpAddrReadIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIpAddrReadIfIndex.setStatus("current")
_HpnicfIpAddrReadAddrType_Type = InetAddressType
_HpnicfIpAddrReadAddrType_Object = MibTableColumn
hpnicfIpAddrReadAddrType = _HpnicfIpAddrReadAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 2, 1, 2),
    _HpnicfIpAddrReadAddrType_Type()
)
hpnicfIpAddrReadAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIpAddrReadAddrType.setStatus("current")
_HpnicfIpAddrReadAddr_Type = InetAddress
_HpnicfIpAddrReadAddr_Object = MibTableColumn
hpnicfIpAddrReadAddr = _HpnicfIpAddrReadAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 2, 1, 3),
    _HpnicfIpAddrReadAddr_Type()
)
hpnicfIpAddrReadAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIpAddrReadAddr.setStatus("current")
_HpnicfIpAddrReadMask_Type = IpAddress
_HpnicfIpAddrReadMask_Object = MibTableColumn
hpnicfIpAddrReadMask = _HpnicfIpAddrReadMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 2, 1, 4),
    _HpnicfIpAddrReadMask_Type()
)
hpnicfIpAddrReadMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpAddrReadMask.setStatus("current")


class _HpnicfIpAddrReadSourceType_Type(Integer32):
    """Custom type hpnicfIpAddrReadSourceType based on Integer32"""
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


_HpnicfIpAddrReadSourceType_Type.__name__ = "Integer32"
_HpnicfIpAddrReadSourceType_Object = MibTableColumn
hpnicfIpAddrReadSourceType = _HpnicfIpAddrReadSourceType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 2, 1, 5),
    _HpnicfIpAddrReadSourceType_Type()
)
hpnicfIpAddrReadSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpAddrReadSourceType.setStatus("current")


class _HpnicfIpAddrReadCatalog_Type(Integer32):
    """Custom type hpnicfIpAddrReadCatalog based on Integer32"""
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


_HpnicfIpAddrReadCatalog_Type.__name__ = "Integer32"
_HpnicfIpAddrReadCatalog_Object = MibTableColumn
hpnicfIpAddrReadCatalog = _HpnicfIpAddrReadCatalog_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 2, 1, 6),
    _HpnicfIpAddrReadCatalog_Type()
)
hpnicfIpAddrReadCatalog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpAddrReadCatalog.setStatus("current")
_HpnicfIpv4AddrTable_Object = MibTable
hpnicfIpv4AddrTable = _HpnicfIpv4AddrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfIpv4AddrTable.setStatus("current")
_HpnicfIpv4AddrEntry_Object = MibTableRow
hpnicfIpv4AddrEntry = _HpnicfIpv4AddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 3, 1)
)
hpnicfIpv4AddrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIpv4AddrEntry.setStatus("current")
_HpnicfIpv4AddrAddr_Type = IpAddress
_HpnicfIpv4AddrAddr_Object = MibTableColumn
hpnicfIpv4AddrAddr = _HpnicfIpv4AddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 3, 1, 1),
    _HpnicfIpv4AddrAddr_Type()
)
hpnicfIpv4AddrAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIpv4AddrAddr.setStatus("current")
_HpnicfIpv4AddrMask_Type = IpAddress
_HpnicfIpv4AddrMask_Object = MibTableColumn
hpnicfIpv4AddrMask = _HpnicfIpv4AddrMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 3, 1, 2),
    _HpnicfIpv4AddrMask_Type()
)
hpnicfIpv4AddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIpv4AddrMask.setStatus("current")
_HpnicfIpv4AddrRowStatus_Type = RowStatus
_HpnicfIpv4AddrRowStatus_Object = MibTableColumn
hpnicfIpv4AddrRowStatus = _HpnicfIpv4AddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 1, 1, 3, 1, 3),
    _HpnicfIpv4AddrRowStatus_Type()
)
hpnicfIpv4AddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIpv4AddrRowStatus.setStatus("current")
_HpnicfIpAddrNotify_ObjectIdentity = ObjectIdentity
hpnicfIpAddrNotify = _HpnicfIpAddrNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 2)
)
_HpnicfIpAddrNotifyScalarObjects_ObjectIdentity = ObjectIdentity
hpnicfIpAddrNotifyScalarObjects = _HpnicfIpAddrNotifyScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 2, 1)
)


class _HpnicfIpAddrNotifyIfIndex_Type(Integer32):
    """Custom type hpnicfIpAddrNotifyIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfIpAddrNotifyIfIndex_Type.__name__ = "Integer32"
_HpnicfIpAddrNotifyIfIndex_Object = MibScalar
hpnicfIpAddrNotifyIfIndex = _HpnicfIpAddrNotifyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 2, 1, 1),
    _HpnicfIpAddrNotifyIfIndex_Type()
)
hpnicfIpAddrNotifyIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfIpAddrNotifyIfIndex.setStatus("current")
_HpnicfIpAddrOldIpAddress_Type = InetAddress
_HpnicfIpAddrOldIpAddress_Object = MibScalar
hpnicfIpAddrOldIpAddress = _HpnicfIpAddrOldIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 2, 1, 2),
    _HpnicfIpAddrOldIpAddress_Type()
)
hpnicfIpAddrOldIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfIpAddrOldIpAddress.setStatus("current")
_HpnicfIpAddrNewIpAddress_Type = InetAddress
_HpnicfIpAddrNewIpAddress_Object = MibScalar
hpnicfIpAddrNewIpAddress = _HpnicfIpAddrNewIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 2, 1, 3),
    _HpnicfIpAddrNewIpAddress_Type()
)
hpnicfIpAddrNewIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfIpAddrNewIpAddress.setStatus("current")
_HpnicfIpAddrFirstTrapTime_Type = TimeTicks
_HpnicfIpAddrFirstTrapTime_Object = MibScalar
hpnicfIpAddrFirstTrapTime = _HpnicfIpAddrFirstTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 2, 1, 4),
    _HpnicfIpAddrFirstTrapTime_Type()
)
hpnicfIpAddrFirstTrapTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfIpAddrFirstTrapTime.setStatus("current")
_HpnicfIpAddrNotifyObjects_ObjectIdentity = ObjectIdentity
hpnicfIpAddrNotifyObjects = _HpnicfIpAddrNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 2, 2)
)
_HpnicfIpAddrNotifyObjectsPrefix_ObjectIdentity = ObjectIdentity
hpnicfIpAddrNotifyObjectsPrefix = _HpnicfIpAddrNotifyObjectsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 2, 2, 0)
)

# Managed Objects groups


# Notification objects

hpnicfIpAddressChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 67, 2, 2, 0, 1)
)
hpnicfIpAddressChangeNotify.setObjects(
      *(("HPN-ICF-IP-ADDRESS-MIB", "hpnicfIpAddrNotifyIfIndex"),
        ("HPN-ICF-IP-ADDRESS-MIB", "hpnicfIpAddrOldIpAddress"),
        ("HPN-ICF-IP-ADDRESS-MIB", "hpnicfIpAddrNewIpAddress"),
        ("HPN-ICF-IP-ADDRESS-MIB", "hpnicfIpAddrFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hpnicfIpAddressChangeNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-IP-ADDRESS-MIB",
    **{"hpnicfIpAddrMIB": hpnicfIpAddrMIB,
       "hpnicfIpAddressObjects": hpnicfIpAddressObjects,
       "hpnicfIpAddressConfig": hpnicfIpAddressConfig,
       "hpnicfIpAddrSetTable": hpnicfIpAddrSetTable,
       "hpnicfIpAddrSetEntry": hpnicfIpAddrSetEntry,
       "hpnicfIpAddrSetIfIndex": hpnicfIpAddrSetIfIndex,
       "hpnicfIpAddrSetAddrType": hpnicfIpAddrSetAddrType,
       "hpnicfIpAddrSetAddr": hpnicfIpAddrSetAddr,
       "hpnicfIpAddrSetMask": hpnicfIpAddrSetMask,
       "hpnicfIpAddrSetSourceType": hpnicfIpAddrSetSourceType,
       "hpnicfIpAddrSetCatalog": hpnicfIpAddrSetCatalog,
       "hpnicfIpAddrSetRowStatus": hpnicfIpAddrSetRowStatus,
       "hpnicfIpAddrReadTable": hpnicfIpAddrReadTable,
       "hpnicfIpAddrReadEntry": hpnicfIpAddrReadEntry,
       "hpnicfIpAddrReadIfIndex": hpnicfIpAddrReadIfIndex,
       "hpnicfIpAddrReadAddrType": hpnicfIpAddrReadAddrType,
       "hpnicfIpAddrReadAddr": hpnicfIpAddrReadAddr,
       "hpnicfIpAddrReadMask": hpnicfIpAddrReadMask,
       "hpnicfIpAddrReadSourceType": hpnicfIpAddrReadSourceType,
       "hpnicfIpAddrReadCatalog": hpnicfIpAddrReadCatalog,
       "hpnicfIpv4AddrTable": hpnicfIpv4AddrTable,
       "hpnicfIpv4AddrEntry": hpnicfIpv4AddrEntry,
       "hpnicfIpv4AddrAddr": hpnicfIpv4AddrAddr,
       "hpnicfIpv4AddrMask": hpnicfIpv4AddrMask,
       "hpnicfIpv4AddrRowStatus": hpnicfIpv4AddrRowStatus,
       "hpnicfIpAddrNotify": hpnicfIpAddrNotify,
       "hpnicfIpAddrNotifyScalarObjects": hpnicfIpAddrNotifyScalarObjects,
       "hpnicfIpAddrNotifyIfIndex": hpnicfIpAddrNotifyIfIndex,
       "hpnicfIpAddrOldIpAddress": hpnicfIpAddrOldIpAddress,
       "hpnicfIpAddrNewIpAddress": hpnicfIpAddrNewIpAddress,
       "hpnicfIpAddrFirstTrapTime": hpnicfIpAddrFirstTrapTime,
       "hpnicfIpAddrNotifyObjects": hpnicfIpAddrNotifyObjects,
       "hpnicfIpAddrNotifyObjectsPrefix": hpnicfIpAddrNotifyObjectsPrefix,
       "hpnicfIpAddressChangeNotify": hpnicfIpAddressChangeNotify}
)
