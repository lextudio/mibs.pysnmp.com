# SNMP MIB module (ONEACCESS-DOT11-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ONEACCESS-DOT11-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:51 2024
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

(oacExpIMDot11,
 oacMIBModules,
 oacRequirements) = mibBuilder.importSymbols(
    "ONEACCESS-GLOBAL-REG",
    "oacExpIMDot11",
    "oacMIBModules",
    "oacRequirements")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

oacDot11MIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 100, 900)
)
oacDot11MIBModule.setRevisions(
        ("2011-10-27 00:00",
         "2010-07-08 00:01")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class InterfaceType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mainInterface", 1),
          ("subInterface", 2))
    )



# MIB Managed Objects in the order of their OIDs

_OacExpIMDot11Conformance_ObjectIdentity = ObjectIdentity
oacExpIMDot11Conformance = _OacExpIMDot11Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 5, 900)
)
_OacExpIMDot11Groups_ObjectIdentity = ObjectIdentity
oacExpIMDot11Groups = _OacExpIMDot11Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 5, 900, 1)
)
_OacExpIMDot11Compliances_ObjectIdentity = ObjectIdentity
oacExpIMDot11Compliances = _OacExpIMDot11Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 5, 900, 2)
)
_OacExpIMDot11Objects_ObjectIdentity = ObjectIdentity
oacExpIMDot11Objects = _OacExpIMDot11Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 8, 1)
)
_OacExpIMDot11InterfaceTable_Object = MibTable
oacExpIMDot11InterfaceTable = _OacExpIMDot11InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 8, 1, 1)
)
if mibBuilder.loadTexts:
    oacExpIMDot11InterfaceTable.setStatus("current")
_OacExpIMDot11InterfaceEntry_Object = MibTableRow
oacExpIMDot11InterfaceEntry = _OacExpIMDot11InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 8, 1, 1, 1)
)
oacExpIMDot11InterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    oacExpIMDot11InterfaceEntry.setStatus("current")
_OacExpIMDot11EntryType_Type = InterfaceType
_OacExpIMDot11EntryType_Object = MibTableColumn
oacExpIMDot11EntryType = _OacExpIMDot11EntryType_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 8, 1, 1, 1, 1),
    _OacExpIMDot11EntryType_Type()
)
oacExpIMDot11EntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacExpIMDot11EntryType.setStatus("current")
_OacExpIMDot11MACAddress_Type = MacAddress
_OacExpIMDot11MACAddress_Object = MibTableColumn
oacExpIMDot11MACAddress = _OacExpIMDot11MACAddress_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 8, 1, 1, 1, 2),
    _OacExpIMDot11MACAddress_Type()
)
oacExpIMDot11MACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacExpIMDot11MACAddress.setStatus("current")


class _OacExpIMDot11SSID_Type(OctetString):
    """Custom type oacExpIMDot11SSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OacExpIMDot11SSID_Type.__name__ = "OctetString"
_OacExpIMDot11SSID_Object = MibTableColumn
oacExpIMDot11SSID = _OacExpIMDot11SSID_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 8, 1, 1, 1, 3),
    _OacExpIMDot11SSID_Type()
)
oacExpIMDot11SSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacExpIMDot11SSID.setStatus("current")
_OacExpIMDot11AssociatedStations_Type = Counter32
_OacExpIMDot11AssociatedStations_Object = MibTableColumn
oacExpIMDot11AssociatedStations = _OacExpIMDot11AssociatedStations_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 8, 1, 1, 1, 4),
    _OacExpIMDot11AssociatedStations_Type()
)
oacExpIMDot11AssociatedStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacExpIMDot11AssociatedStations.setStatus("current")

# Managed Objects groups

oacExpIMDot11GeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13191, 5, 900, 1, 1)
)
oacExpIMDot11GeneralGroup.setObjects(
      *(("ONEACCESS-DOT11-MIB", "oacExpIMDot11EntryType"),
        ("ONEACCESS-DOT11-MIB", "oacExpIMDot11MACAddress"),
        ("ONEACCESS-DOT11-MIB", "oacExpIMDot11SSID"),
        ("ONEACCESS-DOT11-MIB", "oacExpIMDot11AssociatedStations"))
)
if mibBuilder.loadTexts:
    oacExpIMDot11GeneralGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

oacExpIMDot11Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 13191, 5, 900, 2, 1)
)
if mibBuilder.loadTexts:
    oacExpIMDot11Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ONEACCESS-DOT11-MIB",
    **{"InterfaceType": InterfaceType,
       "oacDot11MIBModule": oacDot11MIBModule,
       "oacExpIMDot11Conformance": oacExpIMDot11Conformance,
       "oacExpIMDot11Groups": oacExpIMDot11Groups,
       "oacExpIMDot11GeneralGroup": oacExpIMDot11GeneralGroup,
       "oacExpIMDot11Compliances": oacExpIMDot11Compliances,
       "oacExpIMDot11Compliance": oacExpIMDot11Compliance,
       "oacExpIMDot11Objects": oacExpIMDot11Objects,
       "oacExpIMDot11InterfaceTable": oacExpIMDot11InterfaceTable,
       "oacExpIMDot11InterfaceEntry": oacExpIMDot11InterfaceEntry,
       "oacExpIMDot11EntryType": oacExpIMDot11EntryType,
       "oacExpIMDot11MACAddress": oacExpIMDot11MACAddress,
       "oacExpIMDot11SSID": oacExpIMDot11SSID,
       "oacExpIMDot11AssociatedStations": oacExpIMDot11AssociatedStations}
)
