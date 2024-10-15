# SNMP MIB module (SYMMINTERFACEEXT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYMMINTERFACEEXT
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:53 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(ifEntry,
 ifIndex,
 ifNumber) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifEntry",
    "ifIndex",
    "ifNumber")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(symmInterfaceExtension,) = mibBuilder.importSymbols(
    "SYMM-COMMON-SMI",
    "symmInterfaceExtension")


# MODULE-IDENTITY

symmInterfaceExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1)
)
symmInterfaceExt.setRevisions(
        ("2011-02-24 17:47",)
)


# Types definitions



class CLOCKDIRECTION(Integer32):
    """Custom type CLOCKDIRECTION based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("input", 1),
          ("output", 2),
          ("undefined", 0))
    )




# TEXTUAL-CONVENTIONS



class DateAndTime(OctetString, TextualConvention):
    status = "current"
    displayHint = "2d-1d-1d,1d:1d:1d.1d,1a1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(11, 11),
    )



class TLatAndLon(OctetString, TextualConvention):
    status = "current"
    displayHint = "1a1d:1d:1d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )



class TAntHeight(OctetString, TextualConvention):
    status = "current"
    displayHint = "1a2d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class TLocalTimeOffset(OctetString, TextualConvention):
    status = "current"
    displayHint = "1a1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



class TSsm(Integer32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_InterfaceExtTable_Object = MibTable
interfaceExtTable = _InterfaceExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 1)
)
if mibBuilder.loadTexts:
    interfaceExtTable.setStatus("current")
_InterfaceExtEntry_Object = MibTableRow
interfaceExtEntry = _InterfaceExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    interfaceExtEntry.setStatus("current")
_InterfaceExtType_Type = DisplayString
_InterfaceExtType_Object = MibTableColumn
interfaceExtType = _InterfaceExtType_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 1, 1, 1),
    _InterfaceExtType_Type()
)
interfaceExtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceExtType.setStatus("current")
_InterfaceExtLayer_Type = DisplayString
_InterfaceExtLayer_Object = MibTableColumn
interfaceExtLayer = _InterfaceExtLayer_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 1, 1, 2),
    _InterfaceExtLayer_Type()
)
interfaceExtLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceExtLayer.setStatus("current")
_InterfaceExtEntityIndex_Type = Unsigned32
_InterfaceExtEntityIndex_Object = MibTableColumn
interfaceExtEntityIndex = _InterfaceExtEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 1, 1, 3),
    _InterfaceExtEntityIndex_Type()
)
interfaceExtEntityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceExtEntityIndex.setStatus("current")
_InterfaceExtLocalIndex_Type = Integer32
_InterfaceExtLocalIndex_Object = MibTableColumn
interfaceExtLocalIndex = _InterfaceExtLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 1, 1, 4),
    _InterfaceExtLocalIndex_Type()
)
interfaceExtLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceExtLocalIndex.setStatus("current")
_InterfaceExtSignalDirection_Type = CLOCKDIRECTION
_InterfaceExtSignalDirection_Object = MibTableColumn
interfaceExtSignalDirection = _InterfaceExtSignalDirection_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 1, 1, 5),
    _InterfaceExtSignalDirection_Type()
)
interfaceExtSignalDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceExtSignalDirection.setStatus("current")
_InterfaceExtConformance_ObjectIdentity = ObjectIdentity
interfaceExtConformance = _InterfaceExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 2)
)
if mibBuilder.loadTexts:
    interfaceExtConformance.setStatus("current")
_InterfaceExtCompliances_ObjectIdentity = ObjectIdentity
interfaceExtCompliances = _InterfaceExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 2, 1)
)
_InterfaceExtUocGroups_ObjectIdentity = ObjectIdentity
interfaceExtUocGroups = _InterfaceExtUocGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 2, 2)
)
ifEntry.registerAugmentions(
    ("SYMMINTERFACEEXT",
     "interfaceExtEntry")
)
interfaceExtEntry.setIndexNames(*ifEntry.getIndexNames())

# Managed Objects groups

interfaceExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 2, 2, 1)
)
interfaceExtGroup.setObjects(
      *(("SYMMINTERFACEEXT", "interfaceExtType"),
        ("SYMMINTERFACEEXT", "interfaceExtLayer"),
        ("SYMMINTERFACEEXT", "interfaceExtEntityIndex"),
        ("SYMMINTERFACEEXT", "interfaceExtLocalIndex"),
        ("SYMMINTERFACEEXT", "interfaceExtSignalDirection"))
)
if mibBuilder.loadTexts:
    interfaceExtGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

interfaceExtBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    interfaceExtBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYMMINTERFACEEXT",
    **{"CLOCKDIRECTION": CLOCKDIRECTION,
       "DateAndTime": DateAndTime,
       "TLatAndLon": TLatAndLon,
       "TAntHeight": TAntHeight,
       "TLocalTimeOffset": TLocalTimeOffset,
       "TSsm": TSsm,
       "symmInterfaceExt": symmInterfaceExt,
       "interfaceExtTable": interfaceExtTable,
       "interfaceExtEntry": interfaceExtEntry,
       "interfaceExtType": interfaceExtType,
       "interfaceExtLayer": interfaceExtLayer,
       "interfaceExtEntityIndex": interfaceExtEntityIndex,
       "interfaceExtLocalIndex": interfaceExtLocalIndex,
       "interfaceExtSignalDirection": interfaceExtSignalDirection,
       "interfaceExtConformance": interfaceExtConformance,
       "interfaceExtCompliances": interfaceExtCompliances,
       "interfaceExtBasicCompliance": interfaceExtBasicCompliance,
       "interfaceExtUocGroups": interfaceExtUocGroups,
       "interfaceExtGroup": interfaceExtGroup}
)
