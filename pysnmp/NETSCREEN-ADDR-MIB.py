# SNMP MIB module (NETSCREEN-ADDR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-ADDR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:42 2024
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

(netscreenAddr,) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreenAddr")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

netscreenAddrMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 12, 0)
)
netscreenAddrMibModule.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-03 00:00",
         "2003-11-10 00:00",
         "2001-09-28 00:00",
         "2001-05-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsAddrTable_Object = MibTable
nsAddrTable = _NsAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 12, 1)
)
if mibBuilder.loadTexts:
    nsAddrTable.setStatus("current")
_NsAddrEntry_Object = MibTableRow
nsAddrEntry = _NsAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 12, 1, 1)
)
nsAddrEntry.setIndexNames(
    (0, "NETSCREEN-ADDR-MIB", "nsAddrIndex"),
)
if mibBuilder.loadTexts:
    nsAddrEntry.setStatus("current")


class _NsAddrIndex_Type(Integer32):
    """Custom type nsAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsAddrIndex_Type.__name__ = "Integer32"
_NsAddrIndex_Object = MibTableColumn
nsAddrIndex = _NsAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 12, 1, 1, 1),
    _NsAddrIndex_Type()
)
nsAddrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsAddrIndex.setStatus("current")


class _NsAddrName_Type(DisplayString):
    """Custom type nsAddrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsAddrName_Type.__name__ = "DisplayString"
_NsAddrName_Object = MibTableColumn
nsAddrName = _NsAddrName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 12, 1, 1, 2),
    _NsAddrName_Type()
)
nsAddrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsAddrName.setStatus("current")
_NsAddrVsys_Type = Integer32
_NsAddrVsys_Object = MibTableColumn
nsAddrVsys = _NsAddrVsys_Object(
    (1, 3, 6, 1, 4, 1, 3224, 12, 1, 1, 3),
    _NsAddrVsys_Type()
)
nsAddrVsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsAddrVsys.setStatus("current")
_NsAddrZone_Type = Integer32
_NsAddrZone_Object = MibTableColumn
nsAddrZone = _NsAddrZone_Object(
    (1, 3, 6, 1, 4, 1, 3224, 12, 1, 1, 4),
    _NsAddrZone_Type()
)
nsAddrZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsAddrZone.setStatus("current")


class _NsAddrIpOrDomain_Type(DisplayString):
    """Custom type nsAddrIpOrDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsAddrIpOrDomain_Type.__name__ = "DisplayString"
_NsAddrIpOrDomain_Object = MibTableColumn
nsAddrIpOrDomain = _NsAddrIpOrDomain_Object(
    (1, 3, 6, 1, 4, 1, 3224, 12, 1, 1, 5),
    _NsAddrIpOrDomain_Type()
)
nsAddrIpOrDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsAddrIpOrDomain.setStatus("current")
_NsAddrNetmask_Type = IpAddress
_NsAddrNetmask_Object = MibTableColumn
nsAddrNetmask = _NsAddrNetmask_Object(
    (1, 3, 6, 1, 4, 1, 3224, 12, 1, 1, 6),
    _NsAddrNetmask_Type()
)
nsAddrNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsAddrNetmask.setStatus("current")


class _NsAddrComment_Type(DisplayString):
    """Custom type nsAddrComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsAddrComment_Type.__name__ = "DisplayString"
_NsAddrComment_Object = MibTableColumn
nsAddrComment = _NsAddrComment_Object(
    (1, 3, 6, 1, 4, 1, 3224, 12, 1, 1, 7),
    _NsAddrComment_Type()
)
nsAddrComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsAddrComment.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-ADDR-MIB",
    **{"netscreenAddrMibModule": netscreenAddrMibModule,
       "nsAddrTable": nsAddrTable,
       "nsAddrEntry": nsAddrEntry,
       "nsAddrIndex": nsAddrIndex,
       "nsAddrName": nsAddrName,
       "nsAddrVsys": nsAddrVsys,
       "nsAddrZone": nsAddrZone,
       "nsAddrIpOrDomain": nsAddrIpOrDomain,
       "nsAddrNetmask": nsAddrNetmask,
       "nsAddrComment": nsAddrComment}
)
