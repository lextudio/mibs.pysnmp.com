# SNMP MIB module (ZYXEL-L2-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-L2-IP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:08 2024
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelL2Ip = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelLayer2IpSetup_ObjectIdentity = ObjectIdentity
zyxelLayer2IpSetup = _ZyxelLayer2IpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1)
)
_ZyLayer2IpDnsIpAddress_Type = IpAddress
_ZyLayer2IpDnsIpAddress_Object = MibScalar
zyLayer2IpDnsIpAddress = _ZyLayer2IpDnsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1, 1),
    _ZyLayer2IpDnsIpAddress_Type()
)
zyLayer2IpDnsIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyLayer2IpDnsIpAddress.setStatus("current")


class _ZyLayer2IpDefaultMgmt_Type(Integer32):
    """Custom type zyLayer2IpDefaultMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inBand", 0),
          ("outOfBand", 1))
    )


_ZyLayer2IpDefaultMgmt_Type.__name__ = "Integer32"
_ZyLayer2IpDefaultMgmt_Object = MibScalar
zyLayer2IpDefaultMgmt = _ZyLayer2IpDefaultMgmt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1, 2),
    _ZyLayer2IpDefaultMgmt_Type()
)
zyLayer2IpDefaultMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyLayer2IpDefaultMgmt.setStatus("current")
_ZyxelLayer2IpInbandDefaultSetup_ObjectIdentity = ObjectIdentity
zyxelLayer2IpInbandDefaultSetup = _ZyxelLayer2IpInbandDefaultSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1, 3)
)


class _ZyLayer2IpInbandDefaultType_Type(Integer32):
    """Custom type zyLayer2IpInbandDefaultType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dhcpClient", 0),
          ("staticIp", 1))
    )


_ZyLayer2IpInbandDefaultType_Type.__name__ = "Integer32"
_ZyLayer2IpInbandDefaultType_Object = MibScalar
zyLayer2IpInbandDefaultType = _ZyLayer2IpInbandDefaultType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1, 3, 1),
    _ZyLayer2IpInbandDefaultType_Type()
)
zyLayer2IpInbandDefaultType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyLayer2IpInbandDefaultType.setStatus("current")
_ZyLayer2IpInbandDefaultVid_Type = Integer32
_ZyLayer2IpInbandDefaultVid_Object = MibScalar
zyLayer2IpInbandDefaultVid = _ZyLayer2IpInbandDefaultVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1, 3, 2),
    _ZyLayer2IpInbandDefaultVid_Type()
)
zyLayer2IpInbandDefaultVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyLayer2IpInbandDefaultVid.setStatus("current")
_ZyLayer2IpInbandDefaultStaticIpAddress_Type = IpAddress
_ZyLayer2IpInbandDefaultStaticIpAddress_Object = MibScalar
zyLayer2IpInbandDefaultStaticIpAddress = _ZyLayer2IpInbandDefaultStaticIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1, 3, 3),
    _ZyLayer2IpInbandDefaultStaticIpAddress_Type()
)
zyLayer2IpInbandDefaultStaticIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyLayer2IpInbandDefaultStaticIpAddress.setStatus("current")
_ZyLayer2IpInbandDefaultStaticMask_Type = IpAddress
_ZyLayer2IpInbandDefaultStaticMask_Object = MibScalar
zyLayer2IpInbandDefaultStaticMask = _ZyLayer2IpInbandDefaultStaticMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1, 3, 4),
    _ZyLayer2IpInbandDefaultStaticMask_Type()
)
zyLayer2IpInbandDefaultStaticMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyLayer2IpInbandDefaultStaticMask.setStatus("current")
_ZyLayer2IpInbandDefaultStaticGateway_Type = IpAddress
_ZyLayer2IpInbandDefaultStaticGateway_Object = MibScalar
zyLayer2IpInbandDefaultStaticGateway = _ZyLayer2IpInbandDefaultStaticGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1, 3, 5),
    _ZyLayer2IpInbandDefaultStaticGateway_Type()
)
zyLayer2IpInbandDefaultStaticGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyLayer2IpInbandDefaultStaticGateway.setStatus("current")
_ZyLayer2IpInbandMaxNumberOfInterfaces_Type = Integer32
_ZyLayer2IpInbandMaxNumberOfInterfaces_Object = MibScalar
zyLayer2IpInbandMaxNumberOfInterfaces = _ZyLayer2IpInbandMaxNumberOfInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1, 4),
    _ZyLayer2IpInbandMaxNumberOfInterfaces_Type()
)
zyLayer2IpInbandMaxNumberOfInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyLayer2IpInbandMaxNumberOfInterfaces.setStatus("current")
_ZyxelLayer2IpInbandTable_Object = MibTable
zyxelLayer2IpInbandTable = _ZyxelLayer2IpInbandTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1, 5)
)
if mibBuilder.loadTexts:
    zyxelLayer2IpInbandTable.setStatus("current")
_ZyxelLayer2IpInbandEntry_Object = MibTableRow
zyxelLayer2IpInbandEntry = _ZyxelLayer2IpInbandEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1, 5, 1)
)
zyxelLayer2IpInbandEntry.setIndexNames(
    (0, "ZYXEL-L2-IP-MIB", "zyLayer2IpInbandIpAddress"),
    (0, "ZYXEL-L2-IP-MIB", "zyLayer2IpInbandVid"),
)
if mibBuilder.loadTexts:
    zyxelLayer2IpInbandEntry.setStatus("current")
_ZyLayer2IpInbandIpAddress_Type = IpAddress
_ZyLayer2IpInbandIpAddress_Object = MibTableColumn
zyLayer2IpInbandIpAddress = _ZyLayer2IpInbandIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1, 5, 1, 1),
    _ZyLayer2IpInbandIpAddress_Type()
)
zyLayer2IpInbandIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyLayer2IpInbandIpAddress.setStatus("current")
_ZyLayer2IpInbandMask_Type = IpAddress
_ZyLayer2IpInbandMask_Object = MibTableColumn
zyLayer2IpInbandMask = _ZyLayer2IpInbandMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1, 5, 1, 2),
    _ZyLayer2IpInbandMask_Type()
)
zyLayer2IpInbandMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyLayer2IpInbandMask.setStatus("current")
_ZyLayer2IpInbandGateway_Type = IpAddress
_ZyLayer2IpInbandGateway_Object = MibTableColumn
zyLayer2IpInbandGateway = _ZyLayer2IpInbandGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1, 5, 1, 3),
    _ZyLayer2IpInbandGateway_Type()
)
zyLayer2IpInbandGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyLayer2IpInbandGateway.setStatus("current")
_ZyLayer2IpInbandVid_Type = Integer32
_ZyLayer2IpInbandVid_Object = MibTableColumn
zyLayer2IpInbandVid = _ZyLayer2IpInbandVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1, 5, 1, 4),
    _ZyLayer2IpInbandVid_Type()
)
zyLayer2IpInbandVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyLayer2IpInbandVid.setStatus("current")
_ZyLayer2IpInbandManageableState_Type = EnabledStatus
_ZyLayer2IpInbandManageableState_Object = MibTableColumn
zyLayer2IpInbandManageableState = _ZyLayer2IpInbandManageableState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1, 5, 1, 5),
    _ZyLayer2IpInbandManageableState_Type()
)
zyLayer2IpInbandManageableState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyLayer2IpInbandManageableState.setStatus("current")
_ZyLayer2IpInbandRowStatus_Type = RowStatus
_ZyLayer2IpInbandRowStatus_Object = MibTableColumn
zyLayer2IpInbandRowStatus = _ZyLayer2IpInbandRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 38, 1, 5, 1, 6),
    _ZyLayer2IpInbandRowStatus_Type()
)
zyLayer2IpInbandRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyLayer2IpInbandRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-L2-IP-MIB",
    **{"zyxelL2Ip": zyxelL2Ip,
       "zyxelLayer2IpSetup": zyxelLayer2IpSetup,
       "zyLayer2IpDnsIpAddress": zyLayer2IpDnsIpAddress,
       "zyLayer2IpDefaultMgmt": zyLayer2IpDefaultMgmt,
       "zyxelLayer2IpInbandDefaultSetup": zyxelLayer2IpInbandDefaultSetup,
       "zyLayer2IpInbandDefaultType": zyLayer2IpInbandDefaultType,
       "zyLayer2IpInbandDefaultVid": zyLayer2IpInbandDefaultVid,
       "zyLayer2IpInbandDefaultStaticIpAddress": zyLayer2IpInbandDefaultStaticIpAddress,
       "zyLayer2IpInbandDefaultStaticMask": zyLayer2IpInbandDefaultStaticMask,
       "zyLayer2IpInbandDefaultStaticGateway": zyLayer2IpInbandDefaultStaticGateway,
       "zyLayer2IpInbandMaxNumberOfInterfaces": zyLayer2IpInbandMaxNumberOfInterfaces,
       "zyxelLayer2IpInbandTable": zyxelLayer2IpInbandTable,
       "zyxelLayer2IpInbandEntry": zyxelLayer2IpInbandEntry,
       "zyLayer2IpInbandIpAddress": zyLayer2IpInbandIpAddress,
       "zyLayer2IpInbandMask": zyLayer2IpInbandMask,
       "zyLayer2IpInbandGateway": zyLayer2IpInbandGateway,
       "zyLayer2IpInbandVid": zyLayer2IpInbandVid,
       "zyLayer2IpInbandManageableState": zyLayer2IpInbandManageableState,
       "zyLayer2IpInbandRowStatus": zyLayer2IpInbandRowStatus}
)
