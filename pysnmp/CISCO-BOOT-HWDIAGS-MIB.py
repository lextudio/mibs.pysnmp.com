# SNMP MIB module (CISCO-BOOT-HWDIAGS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-BOOT-HWDIAGS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:20 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoBootHwDiagsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 696)
)
ciscoBootHwDiagsMIB.setRevisions(
        ("2009-05-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoBootHwDiagsMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoBootHwDiagsMIBNotifs = _CiscoBootHwDiagsMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 696, 0)
)
_CiscoBootHwDiagsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoBootHwDiagsMIBObjects = _CiscoBootHwDiagsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 696, 1)
)


class _CiscoBootHwDiagsMIBCurrentBank_Type(Unsigned32):
    """Custom type ciscoBootHwDiagsMIBCurrentBank based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CiscoBootHwDiagsMIBCurrentBank_Type.__name__ = "Unsigned32"
_CiscoBootHwDiagsMIBCurrentBank_Object = MibScalar
ciscoBootHwDiagsMIBCurrentBank = _CiscoBootHwDiagsMIBCurrentBank_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 696, 1, 1),
    _CiscoBootHwDiagsMIBCurrentBank_Type()
)
ciscoBootHwDiagsMIBCurrentBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoBootHwDiagsMIBCurrentBank.setStatus("current")
_CiscoBootHwDiagsMIBTestTable_Object = MibTable
ciscoBootHwDiagsMIBTestTable = _CiscoBootHwDiagsMIBTestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 696, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoBootHwDiagsMIBTestTable.setStatus("current")
_CiscoBootHwDiagsMIBTestEntry_Object = MibTableRow
ciscoBootHwDiagsMIBTestEntry = _CiscoBootHwDiagsMIBTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 696, 1, 2, 1)
)
ciscoBootHwDiagsMIBTestEntry.setIndexNames(
    (0, "CISCO-BOOT-HWDIAGS-MIB", "ciscoBootHwDiagsMIBTestIndex"),
)
if mibBuilder.loadTexts:
    ciscoBootHwDiagsMIBTestEntry.setStatus("current")
_CiscoBootHwDiagsMIBTestIndex_Type = Unsigned32
_CiscoBootHwDiagsMIBTestIndex_Object = MibTableColumn
ciscoBootHwDiagsMIBTestIndex = _CiscoBootHwDiagsMIBTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 696, 1, 2, 1, 1),
    _CiscoBootHwDiagsMIBTestIndex_Type()
)
ciscoBootHwDiagsMIBTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoBootHwDiagsMIBTestIndex.setStatus("current")


class _CiscoBootHwDiagsMIBTestName_Type(DisplayString):
    """Custom type ciscoBootHwDiagsMIBTestName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 255),
    )


_CiscoBootHwDiagsMIBTestName_Type.__name__ = "DisplayString"
_CiscoBootHwDiagsMIBTestName_Object = MibTableColumn
ciscoBootHwDiagsMIBTestName = _CiscoBootHwDiagsMIBTestName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 696, 1, 2, 1, 2),
    _CiscoBootHwDiagsMIBTestName_Type()
)
ciscoBootHwDiagsMIBTestName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoBootHwDiagsMIBTestName.setStatus("current")
_CiscoBootHwDiagsMIBTable_Object = MibTable
ciscoBootHwDiagsMIBTable = _CiscoBootHwDiagsMIBTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 696, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoBootHwDiagsMIBTable.setStatus("current")
_CiscoBootHwDiagsMIBEntry_Object = MibTableRow
ciscoBootHwDiagsMIBEntry = _CiscoBootHwDiagsMIBEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 696, 1, 3, 1)
)
ciscoBootHwDiagsMIBEntry.setIndexNames(
    (0, "CISCO-BOOT-HWDIAGS-MIB", "ciscoBootHwDiagsMIBBankIndex"),
    (0, "CISCO-BOOT-HWDIAGS-MIB", "ciscoBootHwDiagsMIBTestIndex"),
)
if mibBuilder.loadTexts:
    ciscoBootHwDiagsMIBEntry.setStatus("current")


class _CiscoBootHwDiagsMIBBankIndex_Type(Unsigned32):
    """Custom type ciscoBootHwDiagsMIBBankIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CiscoBootHwDiagsMIBBankIndex_Type.__name__ = "Unsigned32"
_CiscoBootHwDiagsMIBBankIndex_Object = MibTableColumn
ciscoBootHwDiagsMIBBankIndex = _CiscoBootHwDiagsMIBBankIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 696, 1, 3, 1, 1),
    _CiscoBootHwDiagsMIBBankIndex_Type()
)
ciscoBootHwDiagsMIBBankIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoBootHwDiagsMIBBankIndex.setStatus("current")


class _CiscoBootHwDiagsMIBLastBootExecuted_Type(TruthValue):
    """Custom type ciscoBootHwDiagsMIBLastBootExecuted based on TruthValue"""


_CiscoBootHwDiagsMIBLastBootExecuted_Object = MibTableColumn
ciscoBootHwDiagsMIBLastBootExecuted = _CiscoBootHwDiagsMIBLastBootExecuted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 696, 1, 3, 1, 2),
    _CiscoBootHwDiagsMIBLastBootExecuted_Type()
)
ciscoBootHwDiagsMIBLastBootExecuted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoBootHwDiagsMIBLastBootExecuted.setStatus("current")
_CiscoBootHwDiagsMIBLastBootPassed_Type = TruthValue
_CiscoBootHwDiagsMIBLastBootPassed_Object = MibTableColumn
ciscoBootHwDiagsMIBLastBootPassed = _CiscoBootHwDiagsMIBLastBootPassed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 696, 1, 3, 1, 3),
    _CiscoBootHwDiagsMIBLastBootPassed_Type()
)
ciscoBootHwDiagsMIBLastBootPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoBootHwDiagsMIBLastBootPassed.setStatus("current")


class _CiscoBootHwDiagsMIBNextBootConfigured_Type(TruthValue):
    """Custom type ciscoBootHwDiagsMIBNextBootConfigured based on TruthValue"""


_CiscoBootHwDiagsMIBNextBootConfigured_Object = MibTableColumn
ciscoBootHwDiagsMIBNextBootConfigured = _CiscoBootHwDiagsMIBNextBootConfigured_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 696, 1, 3, 1, 4),
    _CiscoBootHwDiagsMIBNextBootConfigured_Type()
)
ciscoBootHwDiagsMIBNextBootConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoBootHwDiagsMIBNextBootConfigured.setStatus("current")


class _CiscoBootHwDiagsMIBNextBootArmed_Type(TruthValue):
    """Custom type ciscoBootHwDiagsMIBNextBootArmed based on TruthValue"""


_CiscoBootHwDiagsMIBNextBootArmed_Object = MibTableColumn
ciscoBootHwDiagsMIBNextBootArmed = _CiscoBootHwDiagsMIBNextBootArmed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 696, 1, 3, 1, 5),
    _CiscoBootHwDiagsMIBNextBootArmed_Type()
)
ciscoBootHwDiagsMIBNextBootArmed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoBootHwDiagsMIBNextBootArmed.setStatus("current")


class _CiscoBootHwDiagsMIBConfigCode_Type(Unsigned32):
    """Custom type ciscoBootHwDiagsMIBConfigCode based on Unsigned32"""
    defaultValue = 0


_CiscoBootHwDiagsMIBConfigCode_Object = MibTableColumn
ciscoBootHwDiagsMIBConfigCode = _CiscoBootHwDiagsMIBConfigCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 696, 1, 3, 1, 6),
    _CiscoBootHwDiagsMIBConfigCode_Type()
)
ciscoBootHwDiagsMIBConfigCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoBootHwDiagsMIBConfigCode.setStatus("current")
_CiscoBootHwDiagsMIBResultCode_Type = Unsigned32
_CiscoBootHwDiagsMIBResultCode_Object = MibTableColumn
ciscoBootHwDiagsMIBResultCode = _CiscoBootHwDiagsMIBResultCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 696, 1, 3, 1, 7),
    _CiscoBootHwDiagsMIBResultCode_Type()
)
ciscoBootHwDiagsMIBResultCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoBootHwDiagsMIBResultCode.setStatus("current")
_CiscoBootHwDiagsMIBConform_ObjectIdentity = ObjectIdentity
ciscoBootHwDiagsMIBConform = _CiscoBootHwDiagsMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 696, 2)
)
_CiscoBootHwDiagsMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoBootHwDiagsMIBCompliances = _CiscoBootHwDiagsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 696, 2, 1)
)
_CiscoBootHwDiagsMIBGroups_ObjectIdentity = ObjectIdentity
ciscoBootHwDiagsMIBGroups = _CiscoBootHwDiagsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 696, 2, 2)
)

# Managed Objects groups

ciscoBootHwDiagsMIBMainObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 696, 2, 2, 1)
)
ciscoBootHwDiagsMIBMainObjectGroup.setObjects(
      *(("CISCO-BOOT-HWDIAGS-MIB", "ciscoBootHwDiagsMIBCurrentBank"),
        ("CISCO-BOOT-HWDIAGS-MIB", "ciscoBootHwDiagsMIBTestName"),
        ("CISCO-BOOT-HWDIAGS-MIB", "ciscoBootHwDiagsMIBLastBootExecuted"),
        ("CISCO-BOOT-HWDIAGS-MIB", "ciscoBootHwDiagsMIBLastBootPassed"),
        ("CISCO-BOOT-HWDIAGS-MIB", "ciscoBootHwDiagsMIBNextBootConfigured"),
        ("CISCO-BOOT-HWDIAGS-MIB", "ciscoBootHwDiagsMIBNextBootArmed"),
        ("CISCO-BOOT-HWDIAGS-MIB", "ciscoBootHwDiagsMIBConfigCode"),
        ("CISCO-BOOT-HWDIAGS-MIB", "ciscoBootHwDiagsMIBResultCode"))
)
if mibBuilder.loadTexts:
    ciscoBootHwDiagsMIBMainObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoBootHwDiagsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 696, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoBootHwDiagsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-BOOT-HWDIAGS-MIB",
    **{"ciscoBootHwDiagsMIB": ciscoBootHwDiagsMIB,
       "ciscoBootHwDiagsMIBNotifs": ciscoBootHwDiagsMIBNotifs,
       "ciscoBootHwDiagsMIBObjects": ciscoBootHwDiagsMIBObjects,
       "ciscoBootHwDiagsMIBCurrentBank": ciscoBootHwDiagsMIBCurrentBank,
       "ciscoBootHwDiagsMIBTestTable": ciscoBootHwDiagsMIBTestTable,
       "ciscoBootHwDiagsMIBTestEntry": ciscoBootHwDiagsMIBTestEntry,
       "ciscoBootHwDiagsMIBTestIndex": ciscoBootHwDiagsMIBTestIndex,
       "ciscoBootHwDiagsMIBTestName": ciscoBootHwDiagsMIBTestName,
       "ciscoBootHwDiagsMIBTable": ciscoBootHwDiagsMIBTable,
       "ciscoBootHwDiagsMIBEntry": ciscoBootHwDiagsMIBEntry,
       "ciscoBootHwDiagsMIBBankIndex": ciscoBootHwDiagsMIBBankIndex,
       "ciscoBootHwDiagsMIBLastBootExecuted": ciscoBootHwDiagsMIBLastBootExecuted,
       "ciscoBootHwDiagsMIBLastBootPassed": ciscoBootHwDiagsMIBLastBootPassed,
       "ciscoBootHwDiagsMIBNextBootConfigured": ciscoBootHwDiagsMIBNextBootConfigured,
       "ciscoBootHwDiagsMIBNextBootArmed": ciscoBootHwDiagsMIBNextBootArmed,
       "ciscoBootHwDiagsMIBConfigCode": ciscoBootHwDiagsMIBConfigCode,
       "ciscoBootHwDiagsMIBResultCode": ciscoBootHwDiagsMIBResultCode,
       "ciscoBootHwDiagsMIBConform": ciscoBootHwDiagsMIBConform,
       "ciscoBootHwDiagsMIBCompliances": ciscoBootHwDiagsMIBCompliances,
       "ciscoBootHwDiagsMIBCompliance": ciscoBootHwDiagsMIBCompliance,
       "ciscoBootHwDiagsMIBGroups": ciscoBootHwDiagsMIBGroups,
       "ciscoBootHwDiagsMIBMainObjectGroup": ciscoBootHwDiagsMIBMainObjectGroup}
)
