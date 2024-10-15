# SNMP MIB module (PDN-INET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-INET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:48 2024
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

(pdn_inet,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-inet")

(InetAddressType,) = mibBuilder.importSymbols(
    "PDN-TC",
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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PdnInetMIBObjects_ObjectIdentity = ObjectIdentity
pdnInetMIBObjects = _PdnInetMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1)
)


class _PdnInetTelnetServerPort_Type(Integer32):
    """Custom type pdnInetTelnetServerPort based on Integer32"""
    defaultValue = 23

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PdnInetTelnetServerPort_Type.__name__ = "Integer32"
_PdnInetTelnetServerPort_Object = MibScalar
pdnInetTelnetServerPort = _PdnInetTelnetServerPort_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1, 1),
    _PdnInetTelnetServerPort_Type()
)
pdnInetTelnetServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnInetTelnetServerPort.setStatus("mandatory")


class _PdnInetFtpServerControlPort_Type(Integer32):
    """Custom type pdnInetFtpServerControlPort based on Integer32"""
    defaultValue = 21

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PdnInetFtpServerControlPort_Type.__name__ = "Integer32"
_PdnInetFtpServerControlPort_Object = MibScalar
pdnInetFtpServerControlPort = _PdnInetFtpServerControlPort_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1, 2),
    _PdnInetFtpServerControlPort_Type()
)
pdnInetFtpServerControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnInetFtpServerControlPort.setStatus("mandatory")


class _PdnInetFtpServerDataPort_Type(Integer32):
    """Custom type pdnInetFtpServerDataPort based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PdnInetFtpServerDataPort_Type.__name__ = "Integer32"
_PdnInetFtpServerDataPort_Object = MibScalar
pdnInetFtpServerDataPort = _PdnInetFtpServerDataPort_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1, 3),
    _PdnInetFtpServerDataPort_Type()
)
pdnInetFtpServerDataPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnInetFtpServerDataPort.setStatus("mandatory")
_PdnInetIpAddressTableMaxIpSubnets_Type = Integer32
_PdnInetIpAddressTableMaxIpSubnets_Object = MibScalar
pdnInetIpAddressTableMaxIpSubnets = _PdnInetIpAddressTableMaxIpSubnets_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1, 4),
    _PdnInetIpAddressTableMaxIpSubnets_Type()
)
pdnInetIpAddressTableMaxIpSubnets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnInetIpAddressTableMaxIpSubnets.setStatus("mandatory")
_PdnInetIpAddressTableCurrentIpSubnets_Type = Integer32
_PdnInetIpAddressTableCurrentIpSubnets_Object = MibScalar
pdnInetIpAddressTableCurrentIpSubnets = _PdnInetIpAddressTableCurrentIpSubnets_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1, 5),
    _PdnInetIpAddressTableCurrentIpSubnets_Type()
)
pdnInetIpAddressTableCurrentIpSubnets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnInetIpAddressTableCurrentIpSubnets.setStatus("mandatory")
_PdnInetIpAddressTable_Object = MibTable
pdnInetIpAddressTable = _PdnInetIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1, 6)
)
if mibBuilder.loadTexts:
    pdnInetIpAddressTable.setStatus("mandatory")
_PdnInetIpAddressTableEntry_Object = MibTableRow
pdnInetIpAddressTableEntry = _PdnInetIpAddressTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1, 6, 1)
)
pdnInetIpAddressTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PDN-INET-MIB", "pdnInetIpAddress"),
)
if mibBuilder.loadTexts:
    pdnInetIpAddressTableEntry.setStatus("mandatory")
_PdnInetIpAddress_Type = IpAddress
_PdnInetIpAddress_Object = MibTableColumn
pdnInetIpAddress = _PdnInetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1, 6, 1, 1),
    _PdnInetIpAddress_Type()
)
pdnInetIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnInetIpAddress.setStatus("mandatory")
_PdnInetIpSubnetMask_Type = IpAddress
_PdnInetIpSubnetMask_Object = MibTableColumn
pdnInetIpSubnetMask = _PdnInetIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1, 6, 1, 2),
    _PdnInetIpSubnetMask_Type()
)
pdnInetIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnInetIpSubnetMask.setStatus("mandatory")
_PdnInetIpAddressType_Type = InetAddressType
_PdnInetIpAddressType_Object = MibTableColumn
pdnInetIpAddressType = _PdnInetIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1, 6, 1, 3),
    _PdnInetIpAddressType_Type()
)
pdnInetIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnInetIpAddressType.setStatus("mandatory")
_PdnInetIpRowStatus_Type = RowStatus
_PdnInetIpRowStatus_Object = MibTableColumn
pdnInetIpRowStatus = _PdnInetIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 1, 6, 1, 4),
    _PdnInetIpRowStatus_Type()
)
pdnInetIpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnInetIpRowStatus.setStatus("mandatory")
_PdnInetMIBTraps_ObjectIdentity = ObjectIdentity
pdnInetMIBTraps = _PdnInetMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 26, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-INET-MIB",
    **{"pdnInetMIBObjects": pdnInetMIBObjects,
       "pdnInetTelnetServerPort": pdnInetTelnetServerPort,
       "pdnInetFtpServerControlPort": pdnInetFtpServerControlPort,
       "pdnInetFtpServerDataPort": pdnInetFtpServerDataPort,
       "pdnInetIpAddressTableMaxIpSubnets": pdnInetIpAddressTableMaxIpSubnets,
       "pdnInetIpAddressTableCurrentIpSubnets": pdnInetIpAddressTableCurrentIpSubnets,
       "pdnInetIpAddressTable": pdnInetIpAddressTable,
       "pdnInetIpAddressTableEntry": pdnInetIpAddressTableEntry,
       "pdnInetIpAddress": pdnInetIpAddress,
       "pdnInetIpSubnetMask": pdnInetIpSubnetMask,
       "pdnInetIpAddressType": pdnInetIpAddressType,
       "pdnInetIpRowStatus": pdnInetIpRowStatus,
       "pdnInetMIBTraps": pdnInetMIBTraps}
)
