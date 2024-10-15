# SNMP MIB module (ZYXEL-L3-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-L3-IP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:10 2024
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

zyxelL3Ip = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelLayer3IpSetup_ObjectIdentity = ObjectIdentity
zyxelLayer3IpSetup = _ZyxelLayer3IpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40, 1)
)
_ZyLayer3IpDnsIpAddress_Type = IpAddress
_ZyLayer3IpDnsIpAddress_Object = MibScalar
zyLayer3IpDnsIpAddress = _ZyLayer3IpDnsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40, 1, 1),
    _ZyLayer3IpDnsIpAddress_Type()
)
zyLayer3IpDnsIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyLayer3IpDnsIpAddress.setStatus("current")


class _ZyLayer3IpDefaultMgmt_Type(Integer32):
    """Custom type zyLayer3IpDefaultMgmt based on Integer32"""
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


_ZyLayer3IpDefaultMgmt_Type.__name__ = "Integer32"
_ZyLayer3IpDefaultMgmt_Object = MibScalar
zyLayer3IpDefaultMgmt = _ZyLayer3IpDefaultMgmt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40, 1, 2),
    _ZyLayer3IpDefaultMgmt_Type()
)
zyLayer3IpDefaultMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyLayer3IpDefaultMgmt.setStatus("current")
_ZyLayer3IpDefaultGateway_Type = IpAddress
_ZyLayer3IpDefaultGateway_Object = MibScalar
zyLayer3IpDefaultGateway = _ZyLayer3IpDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40, 1, 3),
    _ZyLayer3IpDefaultGateway_Type()
)
zyLayer3IpDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyLayer3IpDefaultGateway.setStatus("current")
_ZyLayer3IpInbandMaxNumberOfInterfaces_Type = Integer32
_ZyLayer3IpInbandMaxNumberOfInterfaces_Object = MibScalar
zyLayer3IpInbandMaxNumberOfInterfaces = _ZyLayer3IpInbandMaxNumberOfInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40, 1, 4),
    _ZyLayer3IpInbandMaxNumberOfInterfaces_Type()
)
zyLayer3IpInbandMaxNumberOfInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyLayer3IpInbandMaxNumberOfInterfaces.setStatus("current")
_ZyxelLayer3IpInbandTable_Object = MibTable
zyxelLayer3IpInbandTable = _ZyxelLayer3IpInbandTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40, 1, 5)
)
if mibBuilder.loadTexts:
    zyxelLayer3IpInbandTable.setStatus("current")
_ZyxelLayer3IpInbandEntry_Object = MibTableRow
zyxelLayer3IpInbandEntry = _ZyxelLayer3IpInbandEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40, 1, 5, 1)
)
zyxelLayer3IpInbandEntry.setIndexNames(
    (0, "ZYXEL-L3-IP-MIB", "zyLayer3IpInbandIpAddress"),
    (0, "ZYXEL-L3-IP-MIB", "zyLayer3IpInbandMask"),
)
if mibBuilder.loadTexts:
    zyxelLayer3IpInbandEntry.setStatus("current")
_ZyLayer3IpInbandIpAddress_Type = IpAddress
_ZyLayer3IpInbandIpAddress_Object = MibTableColumn
zyLayer3IpInbandIpAddress = _ZyLayer3IpInbandIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40, 1, 5, 1, 1),
    _ZyLayer3IpInbandIpAddress_Type()
)
zyLayer3IpInbandIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyLayer3IpInbandIpAddress.setStatus("current")
_ZyLayer3IpInbandMask_Type = IpAddress
_ZyLayer3IpInbandMask_Object = MibTableColumn
zyLayer3IpInbandMask = _ZyLayer3IpInbandMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40, 1, 5, 1, 2),
    _ZyLayer3IpInbandMask_Type()
)
zyLayer3IpInbandMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyLayer3IpInbandMask.setStatus("current")
_ZyLayer3IpInbandVid_Type = Integer32
_ZyLayer3IpInbandVid_Object = MibTableColumn
zyLayer3IpInbandVid = _ZyLayer3IpInbandVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40, 1, 5, 1, 3),
    _ZyLayer3IpInbandVid_Type()
)
zyLayer3IpInbandVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyLayer3IpInbandVid.setStatus("current")
_ZyLayer3IpInbandRowStatus_Type = RowStatus
_ZyLayer3IpInbandRowStatus_Object = MibTableColumn
zyLayer3IpInbandRowStatus = _ZyLayer3IpInbandRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 40, 1, 5, 1, 4),
    _ZyLayer3IpInbandRowStatus_Type()
)
zyLayer3IpInbandRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyLayer3IpInbandRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-L3-IP-MIB",
    **{"zyxelL3Ip": zyxelL3Ip,
       "zyxelLayer3IpSetup": zyxelLayer3IpSetup,
       "zyLayer3IpDnsIpAddress": zyLayer3IpDnsIpAddress,
       "zyLayer3IpDefaultMgmt": zyLayer3IpDefaultMgmt,
       "zyLayer3IpDefaultGateway": zyLayer3IpDefaultGateway,
       "zyLayer3IpInbandMaxNumberOfInterfaces": zyLayer3IpInbandMaxNumberOfInterfaces,
       "zyxelLayer3IpInbandTable": zyxelLayer3IpInbandTable,
       "zyxelLayer3IpInbandEntry": zyxelLayer3IpInbandEntry,
       "zyLayer3IpInbandIpAddress": zyLayer3IpInbandIpAddress,
       "zyLayer3IpInbandMask": zyLayer3IpInbandMask,
       "zyLayer3IpInbandVid": zyLayer3IpInbandVid,
       "zyLayer3IpInbandRowStatus": zyLayer3IpInbandRowStatus}
)
