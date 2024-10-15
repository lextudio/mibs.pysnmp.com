# SNMP MIB module (IP-INTERFACE-MANAGEMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IP-INTERFACE-MANAGEMENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:33 2024
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

(cjnMgmt,) = mibBuilder.importSymbols(
    "Cajun-ROOT",
    "cjnMgmt")

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

cjnIpIfMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CjnIpIfGroup_ObjectIdentity = ObjectIdentity
cjnIpIfGroup = _CjnIpIfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1)
)
_CjnIpIfNextIndex_Type = Integer32
_CjnIpIfNextIndex_Object = MibScalar
cjnIpIfNextIndex = _CjnIpIfNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 1),
    _CjnIpIfNextIndex_Type()
)
cjnIpIfNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpIfNextIndex.setStatus("current")
_CjnIpIfTable_Object = MibTable
cjnIpIfTable = _CjnIpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cjnIpIfTable.setStatus("current")
_CjnIpIfEntry_Object = MibTableRow
cjnIpIfEntry = _CjnIpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 2, 1)
)
cjnIpIfEntry.setIndexNames(
    (0, "IP-INTERFACE-MANAGEMENT-MIB", "cjnIpIfIndex"),
)
if mibBuilder.loadTexts:
    cjnIpIfEntry.setStatus("current")
_CjnIpIfIndex_Type = Integer32
_CjnIpIfIndex_Object = MibTableColumn
cjnIpIfIndex = _CjnIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 2, 1, 1),
    _CjnIpIfIndex_Type()
)
cjnIpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpIfIndex.setStatus("current")
_CjnIpIfRowStatus_Type = RowStatus
_CjnIpIfRowStatus_Object = MibTableColumn
cjnIpIfRowStatus = _CjnIpIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 2, 1, 2),
    _CjnIpIfRowStatus_Type()
)
cjnIpIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpIfRowStatus.setStatus("current")
_CjnIpIfIpAddress_Type = IpAddress
_CjnIpIfIpAddress_Object = MibTableColumn
cjnIpIfIpAddress = _CjnIpIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 2, 1, 3),
    _CjnIpIfIpAddress_Type()
)
cjnIpIfIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpIfIpAddress.setStatus("current")
_CjnIpIfIpSubnetMask_Type = IpAddress
_CjnIpIfIpSubnetMask_Object = MibTableColumn
cjnIpIfIpSubnetMask = _CjnIpIfIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 2, 1, 4),
    _CjnIpIfIpSubnetMask_Type()
)
cjnIpIfIpSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpIfIpSubnetMask.setStatus("current")


class _CjnIpIfMacFormat_Type(Integer32):
    """Custom type cjnIpIfMacFormat based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ethernetV2", 0),
          ("snap", 1))
    )


_CjnIpIfMacFormat_Type.__name__ = "Integer32"
_CjnIpIfMacFormat_Object = MibTableColumn
cjnIpIfMacFormat = _CjnIpIfMacFormat_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 2, 1, 5),
    _CjnIpIfMacFormat_Type()
)
cjnIpIfMacFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpIfMacFormat.setStatus("current")
_CjnIpIfVlanIfIndex_Type = Integer32
_CjnIpIfVlanIfIndex_Object = MibTableColumn
cjnIpIfVlanIfIndex = _CjnIpIfVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 2, 1, 6),
    _CjnIpIfVlanIfIndex_Type()
)
cjnIpIfVlanIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpIfVlanIfIndex.setStatus("current")


class _CjnIpIfName_Type(OctetString):
    """Custom type cjnIpIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CjnIpIfName_Type.__name__ = "OctetString"
_CjnIpIfName_Object = MibTableColumn
cjnIpIfName = _CjnIpIfName_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 2, 1, 7),
    _CjnIpIfName_Type()
)
cjnIpIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpIfName.setStatus("current")


class _CjnIpIfIpRouting_Type(Integer32):
    """Custom type cjnIpIfIpRouting based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mgmtOnly", 1),
          ("routingAndMgmt", 0),
          ("routingOnly", 2))
    )


_CjnIpIfIpRouting_Type.__name__ = "Integer32"
_CjnIpIfIpRouting_Object = MibTableColumn
cjnIpIfIpRouting = _CjnIpIfIpRouting_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 2, 1, 8),
    _CjnIpIfIpRouting_Type()
)
cjnIpIfIpRouting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpIfIpRouting.setStatus("current")


class _CjnIpIfSpoofCheckEnabled_Type(Integer32):
    """Custom type cjnIpIfSpoofCheckEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CjnIpIfSpoofCheckEnabled_Type.__name__ = "Integer32"
_CjnIpIfSpoofCheckEnabled_Object = MibTableColumn
cjnIpIfSpoofCheckEnabled = _CjnIpIfSpoofCheckEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 2, 1, 9),
    _CjnIpIfSpoofCheckEnabled_Type()
)
cjnIpIfSpoofCheckEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpIfSpoofCheckEnabled.setStatus("current")


class _CjnIpIfProxyArpEnabled_Type(Integer32):
    """Custom type cjnIpIfProxyArpEnabled based on Integer32"""
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


_CjnIpIfProxyArpEnabled_Type.__name__ = "Integer32"
_CjnIpIfProxyArpEnabled_Object = MibTableColumn
cjnIpIfProxyArpEnabled = _CjnIpIfProxyArpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 2, 1, 10),
    _CjnIpIfProxyArpEnabled_Type()
)
cjnIpIfProxyArpEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpIfProxyArpEnabled.setStatus("current")


class _CjnIpIfIcmpRedirEnabled_Type(Integer32):
    """Custom type cjnIpIfIcmpRedirEnabled based on Integer32"""
    defaultValue = 1

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


_CjnIpIfIcmpRedirEnabled_Type.__name__ = "Integer32"
_CjnIpIfIcmpRedirEnabled_Object = MibTableColumn
cjnIpIfIcmpRedirEnabled = _CjnIpIfIcmpRedirEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 2, 1, 11),
    _CjnIpIfIcmpRedirEnabled_Type()
)
cjnIpIfIcmpRedirEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpIfIcmpRedirEnabled.setStatus("current")


class _CjnIpIfUdpRbcastMode_Type(Integer32):
    """Custom type cjnIpIfUdpRbcastMode based on Integer32"""
    defaultValue = 0

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
        *(("both", 3),
          ("disable", 0),
          ("inbound", 1),
          ("outbound", 2))
    )


_CjnIpIfUdpRbcastMode_Type.__name__ = "Integer32"
_CjnIpIfUdpRbcastMode_Object = MibTableColumn
cjnIpIfUdpRbcastMode = _CjnIpIfUdpRbcastMode_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 2, 1, 12),
    _CjnIpIfUdpRbcastMode_Type()
)
cjnIpIfUdpRbcastMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpIfUdpRbcastMode.setStatus("current")


class _CjnIpIfAdminStatus_Type(Integer32):
    """Custom type cjnIpIfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_CjnIpIfAdminStatus_Type.__name__ = "Integer32"
_CjnIpIfAdminStatus_Object = MibTableColumn
cjnIpIfAdminStatus = _CjnIpIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 2, 1, 13),
    _CjnIpIfAdminStatus_Type()
)
cjnIpIfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpIfAdminStatus.setStatus("current")


class _CjnIpIfStatus_Type(Integer32):
    """Custom type cjnIpIfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CjnIpIfStatus_Type.__name__ = "Integer32"
_CjnIpIfStatus_Object = MibTableColumn
cjnIpIfStatus = _CjnIpIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 2, 1, 14),
    _CjnIpIfStatus_Type()
)
cjnIpIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cjnIpIfStatus.setStatus("current")


class _CjnIpIfBootpDhcpGateway_Type(Integer32):
    """Custom type cjnIpIfBootpDhcpGateway based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CjnIpIfBootpDhcpGateway_Type.__name__ = "Integer32"
_CjnIpIfBootpDhcpGateway_Object = MibTableColumn
cjnIpIfBootpDhcpGateway = _CjnIpIfBootpDhcpGateway_Object(
    (1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 2, 1, 15),
    _CjnIpIfBootpDhcpGateway_Type()
)
cjnIpIfBootpDhcpGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cjnIpIfBootpDhcpGateway.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IP-INTERFACE-MANAGEMENT-MIB",
    **{"cjnIpIfMgmt": cjnIpIfMgmt,
       "cjnIpIfGroup": cjnIpIfGroup,
       "cjnIpIfNextIndex": cjnIpIfNextIndex,
       "cjnIpIfTable": cjnIpIfTable,
       "cjnIpIfEntry": cjnIpIfEntry,
       "cjnIpIfIndex": cjnIpIfIndex,
       "cjnIpIfRowStatus": cjnIpIfRowStatus,
       "cjnIpIfIpAddress": cjnIpIfIpAddress,
       "cjnIpIfIpSubnetMask": cjnIpIfIpSubnetMask,
       "cjnIpIfMacFormat": cjnIpIfMacFormat,
       "cjnIpIfVlanIfIndex": cjnIpIfVlanIfIndex,
       "cjnIpIfName": cjnIpIfName,
       "cjnIpIfIpRouting": cjnIpIfIpRouting,
       "cjnIpIfSpoofCheckEnabled": cjnIpIfSpoofCheckEnabled,
       "cjnIpIfProxyArpEnabled": cjnIpIfProxyArpEnabled,
       "cjnIpIfIcmpRedirEnabled": cjnIpIfIcmpRedirEnabled,
       "cjnIpIfUdpRbcastMode": cjnIpIfUdpRbcastMode,
       "cjnIpIfAdminStatus": cjnIpIfAdminStatus,
       "cjnIpIfStatus": cjnIpIfStatus,
       "cjnIpIfBootpDhcpGateway": cjnIpIfBootpDhcpGateway}
)
