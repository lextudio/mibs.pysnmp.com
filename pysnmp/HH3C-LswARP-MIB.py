# SNMP MIB module (HH3C-LswARP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-LswARP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:53 2024
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

(hh3clswCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3clswCommon")

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

hh3cLswArpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 4)
)
hh3cLswArpMib.setRevisions(
        ("2001-06-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cLswProxyArpObject_ObjectIdentity = ObjectIdentity
hh3cLswProxyArpObject = _Hh3cLswProxyArpObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 4, 1)
)
if mibBuilder.loadTexts:
    hh3cLswProxyArpObject.setStatus("current")
_Hh3cLswProxyArpEnableTable_Object = MibTable
hh3cLswProxyArpEnableTable = _Hh3cLswProxyArpEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cLswProxyArpEnableTable.setStatus("current")
_Hh3cLswProxyArpEnableEntry_Object = MibTableRow
hh3cLswProxyArpEnableEntry = _Hh3cLswProxyArpEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 4, 1, 1, 1)
)
hh3cLswProxyArpEnableEntry.setIndexNames(
    (0, "HH3C-LswARP-MIB", "hh3cLswIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cLswProxyArpEnableEntry.setStatus("current")
_Hh3cLswIfIndex_Type = Integer32
_Hh3cLswIfIndex_Object = MibTableColumn
hh3cLswIfIndex = _Hh3cLswIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 4, 1, 1, 1, 1),
    _Hh3cLswIfIndex_Type()
)
hh3cLswIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLswIfIndex.setStatus("current")


class _Hh3cLswProxyArpStatus_Type(Integer32):
    """Custom type hh3cLswProxyArpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Hh3cLswProxyArpStatus_Type.__name__ = "Integer32"
_Hh3cLswProxyArpStatus_Object = MibTableColumn
hh3cLswProxyArpStatus = _Hh3cLswProxyArpStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 4, 1, 1, 1, 2),
    _Hh3cLswProxyArpStatus_Type()
)
hh3cLswProxyArpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLswProxyArpStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-LswARP-MIB",
    **{"hh3cLswArpMib": hh3cLswArpMib,
       "hh3cLswProxyArpObject": hh3cLswProxyArpObject,
       "hh3cLswProxyArpEnableTable": hh3cLswProxyArpEnableTable,
       "hh3cLswProxyArpEnableEntry": hh3cLswProxyArpEnableEntry,
       "hh3cLswIfIndex": hh3cLswIfIndex,
       "hh3cLswProxyArpStatus": hh3cLswProxyArpStatus}
)
