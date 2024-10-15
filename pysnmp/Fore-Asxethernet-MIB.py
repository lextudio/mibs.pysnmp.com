# SNMP MIB module (Fore-Asxethernet-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-Asxethernet-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:51 2024
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

(software,) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "software")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

asxEthernetAutoNegotiate = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 5)
)


# Types definitions



class AsxEthernetModes(Integer32):
    """Custom type AsxEthernetModes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("auto", 5),
          ("hundredFullDuplex", 4),
          ("hundredHalfDuplex", 3),
          ("tenFullDuplex", 2),
          ("tenHalfDuplex", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AsxEthernetAutoNegotiationTable_Object = MibTable
asxEthernetAutoNegotiationTable = _AsxEthernetAutoNegotiationTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 5, 1)
)
if mibBuilder.loadTexts:
    asxEthernetAutoNegotiationTable.setStatus("current")
_AsxEthernetAutoNegotiationEntry_Object = MibTableRow
asxEthernetAutoNegotiationEntry = _AsxEthernetAutoNegotiationEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 5, 1, 1)
)
asxEthernetAutoNegotiationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    asxEthernetAutoNegotiationEntry.setStatus("current")
_AsxEthernetConfigModes_Type = AsxEthernetModes
_AsxEthernetConfigModes_Object = MibTableColumn
asxEthernetConfigModes = _AsxEthernetConfigModes_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 5, 1, 1, 1),
    _AsxEthernetConfigModes_Type()
)
asxEthernetConfigModes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asxEthernetConfigModes.setStatus("current")
_AsxEthernetOperStatus_Type = AsxEthernetModes
_AsxEthernetOperStatus_Object = MibTableColumn
asxEthernetOperStatus = _AsxEthernetOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 5, 1, 1, 2),
    _AsxEthernetOperStatus_Type()
)
asxEthernetOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asxEthernetOperStatus.setStatus("current")


class _AsxEthernetLinkState_Type(Integer32):
    """Custom type asxEthernetLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link-down", 2),
          ("link-up", 1))
    )


_AsxEthernetLinkState_Type.__name__ = "Integer32"
_AsxEthernetLinkState_Object = MibTableColumn
asxEthernetLinkState = _AsxEthernetLinkState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 5, 1, 1, 3),
    _AsxEthernetLinkState_Type()
)
asxEthernetLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asxEthernetLinkState.setStatus("current")


class _AsxEthernetRemoteAutoNeg_Type(Integer32):
    """Custom type asxEthernetRemoteAutoNeg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("detected", 1),
          ("not-detected", 2))
    )


_AsxEthernetRemoteAutoNeg_Type.__name__ = "Integer32"
_AsxEthernetRemoteAutoNeg_Object = MibTableColumn
asxEthernetRemoteAutoNeg = _AsxEthernetRemoteAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 5, 1, 1, 4),
    _AsxEthernetRemoteAutoNeg_Type()
)
asxEthernetRemoteAutoNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asxEthernetRemoteAutoNeg.setStatus("current")


class _AsxEthernetRemoteOperStatus_Type(Integer32):
    """Custom type asxEthernetRemoteOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("hundredFullDuplex", 4),
          ("hundredHalfDuplex", 3),
          ("other", 0),
          ("tenFullDuplex", 2),
          ("tenHalfDuplex", 1))
    )


_AsxEthernetRemoteOperStatus_Type.__name__ = "Integer32"
_AsxEthernetRemoteOperStatus_Object = MibTableColumn
asxEthernetRemoteOperStatus = _AsxEthernetRemoteOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 2, 5, 1, 1, 5),
    _AsxEthernetRemoteOperStatus_Type()
)
asxEthernetRemoteOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asxEthernetRemoteOperStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-Asxethernet-MIB",
    **{"AsxEthernetModes": AsxEthernetModes,
       "asxEthernetAutoNegotiate": asxEthernetAutoNegotiate,
       "asxEthernetAutoNegotiationTable": asxEthernetAutoNegotiationTable,
       "asxEthernetAutoNegotiationEntry": asxEthernetAutoNegotiationEntry,
       "asxEthernetConfigModes": asxEthernetConfigModes,
       "asxEthernetOperStatus": asxEthernetOperStatus,
       "asxEthernetLinkState": asxEthernetLinkState,
       "asxEthernetRemoteAutoNeg": asxEthernetRemoteAutoNeg,
       "asxEthernetRemoteOperStatus": asxEthernetRemoteOperStatus}
)
