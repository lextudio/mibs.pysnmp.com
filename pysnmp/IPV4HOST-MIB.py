# SNMP MIB module (IPV4HOST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPV4HOST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:23 2024
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

(apIpv4Host,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "apIpv4Host")

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

apIpv4HostMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 6, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApIpv4HostTable_Object = MibTable
apIpv4HostTable = _ApIpv4HostTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 6, 2)
)
if mibBuilder.loadTexts:
    apIpv4HostTable.setStatus("current")
_ApIpv4HostEntry_Object = MibTableRow
apIpv4HostEntry = _ApIpv4HostEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 6, 2, 1)
)
apIpv4HostEntry.setIndexNames(
    (0, "IPV4HOST-MIB", "apIpv4HostName"),
)
if mibBuilder.loadTexts:
    apIpv4HostEntry.setStatus("current")


class _ApIpv4HostName_Type(DisplayString):
    """Custom type apIpv4HostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ApIpv4HostName_Type.__name__ = "DisplayString"
_ApIpv4HostName_Object = MibTableColumn
apIpv4HostName = _ApIpv4HostName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 6, 2, 1, 1),
    _ApIpv4HostName_Type()
)
apIpv4HostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4HostName.setStatus("current")
_ApIpv4HostIpAddress_Type = IpAddress
_ApIpv4HostIpAddress_Object = MibTableColumn
apIpv4HostIpAddress = _ApIpv4HostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 6, 2, 1, 2),
    _ApIpv4HostIpAddress_Type()
)
apIpv4HostIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4HostIpAddress.setStatus("current")
_ApIpv4HostStatus_Type = RowStatus
_ApIpv4HostStatus_Object = MibTableColumn
apIpv4HostStatus = _ApIpv4HostStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 6, 2, 1, 3),
    _ApIpv4HostStatus_Type()
)
apIpv4HostStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4HostStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPV4HOST-MIB",
    **{"apIpv4HostMib": apIpv4HostMib,
       "apIpv4HostTable": apIpv4HostTable,
       "apIpv4HostEntry": apIpv4HostEntry,
       "apIpv4HostName": apIpv4HostName,
       "apIpv4HostIpAddress": apIpv4HostIpAddress,
       "apIpv4HostStatus": apIpv4HostStatus}
)
