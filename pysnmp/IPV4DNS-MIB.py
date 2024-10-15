# SNMP MIB module (IPV4DNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPV4DNS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:22 2024
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

(apIpv4Dns,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "apIpv4Dns")

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

apIpv4DnsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 7, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _ApIpv4DnsDefaultSuffix_Type(DisplayString):
    """Custom type apIpv4DnsDefaultSuffix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApIpv4DnsDefaultSuffix_Type.__name__ = "DisplayString"
_ApIpv4DnsDefaultSuffix_Object = MibScalar
apIpv4DnsDefaultSuffix = _ApIpv4DnsDefaultSuffix_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 7, 2),
    _ApIpv4DnsDefaultSuffix_Type()
)
apIpv4DnsDefaultSuffix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4DnsDefaultSuffix.setStatus("current")
_ApIpv4DnsPrimary_Type = IpAddress
_ApIpv4DnsPrimary_Object = MibScalar
apIpv4DnsPrimary = _ApIpv4DnsPrimary_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 7, 3),
    _ApIpv4DnsPrimary_Type()
)
apIpv4DnsPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpv4DnsPrimary.setStatus("current")
_ApIpv4DnsTable_Object = MibTable
apIpv4DnsTable = _ApIpv4DnsTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 7, 4)
)
if mibBuilder.loadTexts:
    apIpv4DnsTable.setStatus("current")
_ApIpv4DnsEntry_Object = MibTableRow
apIpv4DnsEntry = _ApIpv4DnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 7, 4, 1)
)
apIpv4DnsEntry.setIndexNames(
    (0, "IPV4DNS-MIB", "apIpv4DnsSecondaryIP"),
)
if mibBuilder.loadTexts:
    apIpv4DnsEntry.setStatus("current")
_ApIpv4DnsSecondaryIP_Type = IpAddress
_ApIpv4DnsSecondaryIP_Object = MibTableColumn
apIpv4DnsSecondaryIP = _ApIpv4DnsSecondaryIP_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 7, 4, 1, 1),
    _ApIpv4DnsSecondaryIP_Type()
)
apIpv4DnsSecondaryIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIpv4DnsSecondaryIP.setStatus("current")
_ApIpv4DnsStatus_Type = RowStatus
_ApIpv4DnsStatus_Object = MibTableColumn
apIpv4DnsStatus = _ApIpv4DnsStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 9, 7, 4, 1, 2),
    _ApIpv4DnsStatus_Type()
)
apIpv4DnsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIpv4DnsStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPV4DNS-MIB",
    **{"apIpv4DnsMib": apIpv4DnsMib,
       "apIpv4DnsDefaultSuffix": apIpv4DnsDefaultSuffix,
       "apIpv4DnsPrimary": apIpv4DnsPrimary,
       "apIpv4DnsTable": apIpv4DnsTable,
       "apIpv4DnsEntry": apIpv4DnsEntry,
       "apIpv4DnsSecondaryIP": apIpv4DnsSecondaryIP,
       "apIpv4DnsStatus": apIpv4DnsStatus}
)
