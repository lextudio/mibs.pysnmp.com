# SNMP MIB module (GW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:21 2024
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
 enterprises,
 experimental,
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
    "enterprises",
    "experimental",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Usr_ObjectIdentity = ObjectIdentity
usr = _Usr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429)
)
_Nas_ObjectIdentity = ObjectIdentity
nas = _Nas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1)
)
_Gw_ObjectIdentity = ObjectIdentity
gw = _Gw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 18)
)
_GwTe_ObjectIdentity = ObjectIdentity
gwTe = _GwTe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 18, 1)
)
_GwTeTable_Object = MibTable
gwTeTable = _GwTeTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 18, 1, 1)
)
if mibBuilder.loadTexts:
    gwTeTable.setStatus("mandatory")
_GwTeEntry_Object = MibTableRow
gwTeEntry = _GwTeEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 18, 1, 1, 1)
)
gwTeEntry.setIndexNames(
    (0, "GW-MIB", "gwTeIndex"),
)
if mibBuilder.loadTexts:
    gwTeEntry.setStatus("mandatory")
_GwTeIndex_Type = Integer32
_GwTeIndex_Object = MibTableColumn
gwTeIndex = _GwTeIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 18, 1, 1, 1, 1),
    _GwTeIndex_Type()
)
gwTeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwTeIndex.setStatus("mandatory")


class _GwTegwNetworkFailed_Type(Integer32):
    """Custom type gwTegwNetworkFailed based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_GwTegwNetworkFailed_Type.__name__ = "Integer32"
_GwTegwNetworkFailed_Object = MibTableColumn
gwTegwNetworkFailed = _GwTegwNetworkFailed_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 18, 1, 1, 1, 2),
    _GwTegwNetworkFailed_Type()
)
gwTegwNetworkFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwTegwNetworkFailed.setStatus("mandatory")


class _GwTegwNetworkRestored_Type(Integer32):
    """Custom type gwTegwNetworkRestored based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_GwTegwNetworkRestored_Type.__name__ = "Integer32"
_GwTegwNetworkRestored_Object = MibTableColumn
gwTegwNetworkRestored = _GwTegwNetworkRestored_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 18, 1, 1, 1, 3),
    _GwTegwNetworkRestored_Type()
)
gwTegwNetworkRestored.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwTegwNetworkRestored.setStatus("mandatory")
_GwTegwIPAddress_Type = IpAddress
_GwTegwIPAddress_Object = MibTableColumn
gwTegwIPAddress = _GwTegwIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 18, 1, 1, 1, 4),
    _GwTegwIPAddress_Type()
)
gwTegwIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwTegwIPAddress.setStatus("mandatory")


class _GwTeArNetFailed_Type(OctetString):
    """Custom type gwTeArNetFailed based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_GwTeArNetFailed_Type.__name__ = "OctetString"
_GwTeArNetFailed_Object = MibTableColumn
gwTeArNetFailed = _GwTeArNetFailed_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 18, 1, 1, 1, 5),
    _GwTeArNetFailed_Type()
)
gwTeArNetFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwTeArNetFailed.setStatus("mandatory")


class _GwTeArNetRestored_Type(OctetString):
    """Custom type gwTeArNetRestored based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_GwTeArNetRestored_Type.__name__ = "OctetString"
_GwTeArNetRestored_Object = MibTableColumn
gwTeArNetRestored = _GwTeArNetRestored_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 18, 1, 1, 1, 6),
    _GwTeArNetRestored_Type()
)
gwTeArNetRestored.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwTeArNetRestored.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GW-MIB",
    **{"usr": usr,
       "nas": nas,
       "gw": gw,
       "gwTe": gwTe,
       "gwTeTable": gwTeTable,
       "gwTeEntry": gwTeEntry,
       "gwTeIndex": gwTeIndex,
       "gwTegwNetworkFailed": gwTegwNetworkFailed,
       "gwTegwNetworkRestored": gwTegwNetworkRestored,
       "gwTegwIPAddress": gwTegwIPAddress,
       "gwTeArNetFailed": gwTeArNetFailed,
       "gwTeArNetRestored": gwTeArNetRestored}
)
