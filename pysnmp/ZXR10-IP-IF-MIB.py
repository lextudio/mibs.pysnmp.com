# SNMP MIB module (ZXR10-IP-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZXR10-IP-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:53 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(zxr10interfaces,) = mibBuilder.importSymbols(
    "ZXR10-SMI",
    "zxr10interfaces")


# MODULE-IDENTITY

zxr10IPIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 1)
)
zxr10IPIfMIB.setRevisions(
        ("2005-04-12 00:00",)
)


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zxr10IPIfMIBObjects_ObjectIdentity = ObjectIdentity
zxr10IPIfMIBObjects = _Zxr10IPIfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 1, 1)
)
_Zxr10IPAddressConfiguration_ObjectIdentity = ObjectIdentity
zxr10IPAddressConfiguration = _Zxr10IPAddressConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 1, 1, 1)
)
_Zxr10IPAddrTable_Object = MibTable
zxr10IPAddrTable = _Zxr10IPAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    zxr10IPAddrTable.setStatus("current")
_Zxr10IPAddrEntry_Object = MibTableRow
zxr10IPAddrEntry = _Zxr10IPAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 1, 1, 1, 1, 1)
)
zxr10IPAddrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxr10IPAddrEntry.setStatus("current")
_Zxr10IPAddrPrimaryIp_Type = IpAddress
_Zxr10IPAddrPrimaryIp_Object = MibTableColumn
zxr10IPAddrPrimaryIp = _Zxr10IPAddrPrimaryIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 1, 1, 1, 1, 1, 1),
    _Zxr10IPAddrPrimaryIp_Type()
)
zxr10IPAddrPrimaryIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10IPAddrPrimaryIp.setStatus("current")
_Zxr10IPAddrPrimaryIpMask_Type = IpAddress
_Zxr10IPAddrPrimaryIpMask_Object = MibTableColumn
zxr10IPAddrPrimaryIpMask = _Zxr10IPAddrPrimaryIpMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 1, 1, 1, 1, 1, 2),
    _Zxr10IPAddrPrimaryIpMask_Type()
)
zxr10IPAddrPrimaryIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10IPAddrPrimaryIpMask.setStatus("current")
_Zxr10IPAddrBroadcast_Type = IpAddress
_Zxr10IPAddrBroadcast_Object = MibTableColumn
zxr10IPAddrBroadcast = _Zxr10IPAddrBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 1, 1, 1, 1, 1, 3),
    _Zxr10IPAddrBroadcast_Type()
)
zxr10IPAddrBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10IPAddrBroadcast.setStatus("current")
_Zxr10IPAddrRowStatus_Type = RowStatus
_Zxr10IPAddrRowStatus_Object = MibTableColumn
zxr10IPAddrRowStatus = _Zxr10IPAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 1, 1, 1, 1, 1, 4),
    _Zxr10IPAddrRowStatus_Type()
)
zxr10IPAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10IPAddrRowStatus.setStatus("current")


class _Zxr10IPAddrIfName_Type(DisplayString):
    """Custom type zxr10IPAddrIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10IPAddrIfName_Type.__name__ = "DisplayString"
_Zxr10IPAddrIfName_Object = MibTableColumn
zxr10IPAddrIfName = _Zxr10IPAddrIfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 1, 1, 1, 1, 1, 5),
    _Zxr10IPAddrIfName_Type()
)
zxr10IPAddrIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10IPAddrIfName.setStatus("current")
_Zxr10IPSecondaryAddrTable_Object = MibTable
zxr10IPSecondaryAddrTable = _Zxr10IPSecondaryAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    zxr10IPSecondaryAddrTable.setStatus("current")
_Zxr10IPSecondaryAddrEnry_Object = MibTableRow
zxr10IPSecondaryAddrEnry = _Zxr10IPSecondaryAddrEnry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 1, 1, 1, 2, 1)
)
zxr10IPSecondaryAddrEnry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZXR10-IP-IF-MIB", "zxr10IPSecondaryAddr"),
)
if mibBuilder.loadTexts:
    zxr10IPSecondaryAddrEnry.setStatus("current")
_Zxr10IPSecondaryAddr_Type = IpAddress
_Zxr10IPSecondaryAddr_Object = MibTableColumn
zxr10IPSecondaryAddr = _Zxr10IPSecondaryAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 1, 1, 1, 2, 1, 1),
    _Zxr10IPSecondaryAddr_Type()
)
zxr10IPSecondaryAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10IPSecondaryAddr.setStatus("current")
_Zxr10IPSecondaryAddrMask_Type = IpAddress
_Zxr10IPSecondaryAddrMask_Object = MibTableColumn
zxr10IPSecondaryAddrMask = _Zxr10IPSecondaryAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 1, 1, 1, 2, 1, 2),
    _Zxr10IPSecondaryAddrMask_Type()
)
zxr10IPSecondaryAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10IPSecondaryAddrMask.setStatus("current")
_Zxr10IPSecondaryAddrRowStatus_Type = RowStatus
_Zxr10IPSecondaryAddrRowStatus_Object = MibTableColumn
zxr10IPSecondaryAddrRowStatus = _Zxr10IPSecondaryAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 1, 1, 1, 2, 1, 3),
    _Zxr10IPSecondaryAddrRowStatus_Type()
)
zxr10IPSecondaryAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10IPSecondaryAddrRowStatus.setStatus("current")


class _Zxr10IPSecondaryIfName_Type(DisplayString):
    """Custom type zxr10IPSecondaryIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10IPSecondaryIfName_Type.__name__ = "DisplayString"
_Zxr10IPSecondaryIfName_Object = MibTableColumn
zxr10IPSecondaryIfName = _Zxr10IPSecondaryIfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 1, 1, 1, 2, 1, 4),
    _Zxr10IPSecondaryIfName_Type()
)
zxr10IPSecondaryIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10IPSecondaryIfName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXR10-IP-IF-MIB",
    **{"DisplayString": DisplayString,
       "zxr10IPIfMIB": zxr10IPIfMIB,
       "zxr10IPIfMIBObjects": zxr10IPIfMIBObjects,
       "zxr10IPAddressConfiguration": zxr10IPAddressConfiguration,
       "zxr10IPAddrTable": zxr10IPAddrTable,
       "zxr10IPAddrEntry": zxr10IPAddrEntry,
       "zxr10IPAddrPrimaryIp": zxr10IPAddrPrimaryIp,
       "zxr10IPAddrPrimaryIpMask": zxr10IPAddrPrimaryIpMask,
       "zxr10IPAddrBroadcast": zxr10IPAddrBroadcast,
       "zxr10IPAddrRowStatus": zxr10IPAddrRowStatus,
       "zxr10IPAddrIfName": zxr10IPAddrIfName,
       "zxr10IPSecondaryAddrTable": zxr10IPSecondaryAddrTable,
       "zxr10IPSecondaryAddrEnry": zxr10IPSecondaryAddrEnry,
       "zxr10IPSecondaryAddr": zxr10IPSecondaryAddr,
       "zxr10IPSecondaryAddrMask": zxr10IPSecondaryAddrMask,
       "zxr10IPSecondaryAddrRowStatus": zxr10IPSecondaryAddrRowStatus,
       "zxr10IPSecondaryIfName": zxr10IPSecondaryIfName}
)
