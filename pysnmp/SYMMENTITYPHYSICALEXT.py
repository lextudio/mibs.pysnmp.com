# SNMP MIB module (SYMMENTITYPHYSICALEXT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYMMENTITYPHYSICALEXT
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:50 2024
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

(entPhysicalEntry,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalEntry",
    "entPhysicalIndex")

(ifIndex,
 ifNumber) = mibBuilder.importSymbols(
    "IF-MIB",
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

(symmEntPhysicalExtension,) = mibBuilder.importSymbols(
    "SYMM-COMMON-SMI",
    "symmEntPhysicalExtension")


# MODULE-IDENTITY

symmEntityPhysicalExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1)
)
symmEntityPhysicalExt.setRevisions(
        ("2016-06-15 10:39",)
)


# Types definitions


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

_EntPhysicalExtTable_Object = MibTable
entPhysicalExtTable = _EntPhysicalExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 1)
)
if mibBuilder.loadTexts:
    entPhysicalExtTable.setStatus("current")
_EntPhysicalExtEntry_Object = MibTableRow
entPhysicalExtEntry = _EntPhysicalExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    entPhysicalExtEntry.setStatus("current")
_EntPhyInService_Type = DisplayString
_EntPhyInService_Object = MibTableColumn
entPhyInService = _EntPhyInService_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 1, 1, 1),
    _EntPhyInService_Type()
)
entPhyInService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhyInService.setStatus("current")
_EntPhyCLEINum_Type = DisplayString
_EntPhyCLEINum_Object = MibTableColumn
entPhyCLEINum = _EntPhyCLEINum_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 1, 1, 2),
    _EntPhyCLEINum_Type()
)
entPhyCLEINum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhyCLEINum.setStatus("current")
_EntPhyFPGAVersion_Type = DisplayString
_EntPhyFPGAVersion_Object = MibTableColumn
entPhyFPGAVersion = _EntPhyFPGAVersion_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 1, 1, 3),
    _EntPhyFPGAVersion_Type()
)
entPhyFPGAVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhyFPGAVersion.setStatus("current")
_EntPhySlot_Type = DisplayString
_EntPhySlot_Object = MibTableColumn
entPhySlot = _EntPhySlot_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 1, 1, 4),
    _EntPhySlot_Type()
)
entPhySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhySlot.setStatus("current")
_EntPhyCompatiHW_Type = DisplayString
_EntPhyCompatiHW_Object = MibTableColumn
entPhyCompatiHW = _EntPhyCompatiHW_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 1, 1, 5),
    _EntPhyCompatiHW_Type()
)
entPhyCompatiHW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhyCompatiHW.setStatus("current")
_EntPhyCompatiSW_Type = DisplayString
_EntPhyCompatiSW_Object = MibTableColumn
entPhyCompatiSW = _EntPhyCompatiSW_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 1, 1, 6),
    _EntPhyCompatiSW_Type()
)
entPhyCompatiSW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhyCompatiSW.setStatus("current")
_EntPhyCompatiMtoM_Type = DisplayString
_EntPhyCompatiMtoM_Object = MibTableColumn
entPhyCompatiMtoM = _EntPhyCompatiMtoM_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 1, 1, 7),
    _EntPhyCompatiMtoM_Type()
)
entPhyCompatiMtoM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhyCompatiMtoM.setStatus("current")
_EntPhyCountryOfOrigin_Type = DisplayString
_EntPhyCountryOfOrigin_Object = MibTableColumn
entPhyCountryOfOrigin = _EntPhyCountryOfOrigin_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 1, 1, 8),
    _EntPhyCountryOfOrigin_Type()
)
entPhyCountryOfOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhyCountryOfOrigin.setStatus("current")
_EntPhyManufacturerID_Type = DisplayString
_EntPhyManufacturerID_Object = MibTableColumn
entPhyManufacturerID = _EntPhyManufacturerID_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 1, 1, 9),
    _EntPhyManufacturerID_Type()
)
entPhyManufacturerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entPhyManufacturerID.setStatus("current")
_EntPhysicalExtConformance_ObjectIdentity = ObjectIdentity
entPhysicalExtConformance = _EntPhysicalExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 2)
)
if mibBuilder.loadTexts:
    entPhysicalExtConformance.setStatus("current")
_EntPhysicalExtCompliances_ObjectIdentity = ObjectIdentity
entPhysicalExtCompliances = _EntPhysicalExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 2, 1)
)
_EntPhysicalExtUocGroups_ObjectIdentity = ObjectIdentity
entPhysicalExtUocGroups = _EntPhysicalExtUocGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 2, 2)
)
entPhysicalEntry.registerAugmentions(
    ("SYMMENTITYPHYSICALEXT",
     "entPhysicalExtEntry")
)
entPhysicalExtEntry.setIndexNames(*entPhysicalEntry.getIndexNames())

# Managed Objects groups

entPhysicalExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 2, 2, 1)
)
entPhysicalExtGroup.setObjects(
      *(("SYMMENTITYPHYSICALEXT", "entPhyInService"),
        ("SYMMENTITYPHYSICALEXT", "entPhyCLEINum"),
        ("SYMMENTITYPHYSICALEXT", "entPhyFPGAVersion"),
        ("SYMMENTITYPHYSICALEXT", "entPhySlot"),
        ("SYMMENTITYPHYSICALEXT", "entPhyCompatiHW"),
        ("SYMMENTITYPHYSICALEXT", "entPhyCompatiSW"),
        ("SYMMENTITYPHYSICALEXT", "entPhyCompatiMtoM"),
        ("SYMMENTITYPHYSICALEXT", "entPhyCountryOfOrigin"),
        ("SYMMENTITYPHYSICALEXT", "entPhyManufacturerID"))
)
if mibBuilder.loadTexts:
    entPhysicalExtGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

entPhysicalExtBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 5, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    entPhysicalExtBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYMMENTITYPHYSICALEXT",
    **{"DateAndTime": DateAndTime,
       "TLatAndLon": TLatAndLon,
       "TAntHeight": TAntHeight,
       "TLocalTimeOffset": TLocalTimeOffset,
       "TSsm": TSsm,
       "symmEntityPhysicalExt": symmEntityPhysicalExt,
       "entPhysicalExtTable": entPhysicalExtTable,
       "entPhysicalExtEntry": entPhysicalExtEntry,
       "entPhyInService": entPhyInService,
       "entPhyCLEINum": entPhyCLEINum,
       "entPhyFPGAVersion": entPhyFPGAVersion,
       "entPhySlot": entPhySlot,
       "entPhyCompatiHW": entPhyCompatiHW,
       "entPhyCompatiSW": entPhyCompatiSW,
       "entPhyCompatiMtoM": entPhyCompatiMtoM,
       "entPhyCountryOfOrigin": entPhyCountryOfOrigin,
       "entPhyManufacturerID": entPhyManufacturerID,
       "entPhysicalExtConformance": entPhysicalExtConformance,
       "entPhysicalExtCompliances": entPhysicalExtCompliances,
       "entPhysicalExtBasicCompliance": entPhysicalExtBasicCompliance,
       "entPhysicalExtUocGroups": entPhysicalExtUocGroups,
       "entPhysicalExtGroup": entPhysicalExtGroup}
)
