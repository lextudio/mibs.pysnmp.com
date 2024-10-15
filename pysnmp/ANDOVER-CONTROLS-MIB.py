# SNMP MIB module (ANDOVER-CONTROLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ANDOVER-CONTROLS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:39 2024
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
 enterprises,
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
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

andoverControls = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10829)
)
andoverControls.setRevisions(
        ("2002-10-30 09:46",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AccAlarmAgent_ObjectIdentity = ObjectIdentity
accAlarmAgent = _AccAlarmAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10829, 1)
)
if mibBuilder.loadTexts:
    accAlarmAgent.setStatus("deprecated")
_AccCommon_ObjectIdentity = ObjectIdentity
accCommon = _AccCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10829, 4)
)
if mibBuilder.loadTexts:
    accCommon.setStatus("current")
_AccProduct_ObjectIdentity = ObjectIdentity
accProduct = _AccProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10829, 5)
)
if mibBuilder.loadTexts:
    accProduct.setStatus("current")
_AccInfinetController_ObjectIdentity = ObjectIdentity
accInfinetController = _AccInfinetController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10829, 5, 1)
)
_AccNetController_ObjectIdentity = ObjectIdentity
accNetController = _AccNetController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10829, 5, 2)
)
_AccFrontEnd_ObjectIdentity = ObjectIdentity
accFrontEnd = _AccFrontEnd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10829, 5, 3)
)
_AccSystem_ObjectIdentity = ObjectIdentity
accSystem = _AccSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10829, 6)
)
if mibBuilder.loadTexts:
    accSystem.setStatus("current")


class _AccModel_Type(DisplayString):
    """Custom type accModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AccModel_Type.__name__ = "DisplayString"
_AccModel_Object = MibScalar
accModel = _AccModel_Object(
    (1, 3, 6, 1, 4, 1, 10829, 6, 1),
    _AccModel_Type()
)
accModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accModel.setStatus("current")


class _AccFirmwareVersion_Type(DisplayString):
    """Custom type accFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AccFirmwareVersion_Type.__name__ = "DisplayString"
_AccFirmwareVersion_Object = MibScalar
accFirmwareVersion = _AccFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 10829, 6, 2),
    _AccFirmwareVersion_Type()
)
accFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFirmwareVersion.setStatus("current")
_AccConformance_ObjectIdentity = ObjectIdentity
accConformance = _AccConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10829, 7)
)
_AccGroups_ObjectIdentity = ObjectIdentity
accGroups = _AccGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10829, 7, 2)
)
_AccCompliance_ObjectIdentity = ObjectIdentity
accCompliance = _AccCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10829, 7, 3)
)

# Managed Objects groups

accSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10829, 7, 2, 1)
)
accSystemGroup.setObjects(
      *(("ANDOVER-CONTROLS-MIB", "accModel"),
        ("ANDOVER-CONTROLS-MIB", "accFirmwareVersion"))
)
if mibBuilder.loadTexts:
    accSystemGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

accBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 10829, 7, 3, 1)
)
if mibBuilder.loadTexts:
    accBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ANDOVER-CONTROLS-MIB",
    **{"andoverControls": andoverControls,
       "accAlarmAgent": accAlarmAgent,
       "accCommon": accCommon,
       "accProduct": accProduct,
       "accInfinetController": accInfinetController,
       "accNetController": accNetController,
       "accFrontEnd": accFrontEnd,
       "accSystem": accSystem,
       "accModel": accModel,
       "accFirmwareVersion": accFirmwareVersion,
       "accConformance": accConformance,
       "accGroups": accGroups,
       "accSystemGroup": accSystemGroup,
       "accCompliance": accCompliance,
       "accBasicCompliance": accBasicCompliance}
)
