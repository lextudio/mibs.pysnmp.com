# SNMP MIB module (DOCS-TEST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DOCS-TEST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:10 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

docsTestMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 12)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CableLabs_ObjectIdentity = ObjectIdentity
cableLabs = _CableLabs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491)
)
_ClabFunction_ObjectIdentity = ObjectIdentity
clabFunction = _ClabFunction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 1)
)
_ClabFuncMib2_ObjectIdentity = ObjectIdentity
clabFuncMib2 = _ClabFuncMib2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 1, 1)
)
_ClabFuncProprietary_ObjectIdentity = ObjectIdentity
clabFuncProprietary = _ClabFuncProprietary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 1, 2)
)
_ClabProject_ObjectIdentity = ObjectIdentity
clabProject = _ClabProject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2)
)
_ClabProjDocsis_ObjectIdentity = ObjectIdentity
clabProjDocsis = _ClabProjDocsis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1)
)
_DocsTestMibObjects_ObjectIdentity = ObjectIdentity
docsTestMibObjects = _DocsTestMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 1)
)
_DocsTestBaseObjects_ObjectIdentity = ObjectIdentity
docsTestBaseObjects = _DocsTestBaseObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 1, 1)
)
_DocsTestCapability_Type = OctetString
_DocsTestCapability_Object = MibScalar
docsTestCapability = _DocsTestCapability_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 1, 1, 1),
    _DocsTestCapability_Type()
)
docsTestCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsTestCapability.setStatus("current")
_DocsTestStatus_Type = OctetString
_DocsTestStatus_Object = MibScalar
docsTestStatus = _DocsTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 1, 1, 2),
    _DocsTestStatus_Type()
)
docsTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsTestStatus.setStatus("current")
_DocsTestSetupObjects_ObjectIdentity = ObjectIdentity
docsTestSetupObjects = _DocsTestSetupObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 1, 2)
)


class _DocsTestType_Type(Integer32):
    """Custom type docsTestType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_DocsTestType_Type.__name__ = "Integer32"
_DocsTestType_Object = MibScalar
docsTestType = _DocsTestType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 1, 2, 1),
    _DocsTestType_Type()
)
docsTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsTestType.setStatus("current")
_DocsTestData_Type = OctetString
_DocsTestData_Object = MibScalar
docsTestData = _DocsTestData_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 1, 2, 2),
    _DocsTestData_Type()
)
docsTestData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsTestData.setStatus("current")
_DocsTestEnable_Type = TruthValue
_DocsTestEnable_Object = MibScalar
docsTestEnable = _DocsTestEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 1, 2, 3),
    _DocsTestEnable_Type()
)
docsTestEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsTestEnable.setStatus("current")
_DocsTestConformance_ObjectIdentity = ObjectIdentity
docsTestConformance = _DocsTestConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 2)
)
_DocsTestCompliances_ObjectIdentity = ObjectIdentity
docsTestCompliances = _DocsTestCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 2, 1)
)
_DocsTestGroups_ObjectIdentity = ObjectIdentity
docsTestGroups = _DocsTestGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 2, 2)
)
_ClabProjPacketCable_ObjectIdentity = ObjectIdentity
clabProjPacketCable = _ClabProjPacketCable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2)
)
_ClabProjOpenCable_ObjectIdentity = ObjectIdentity
clabProjOpenCable = _ClabProjOpenCable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 3)
)
_ClabProjCableHome_ObjectIdentity = ObjectIdentity
clabProjCableHome = _ClabProjCableHome_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4)
)

# Managed Objects groups

docsTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 2, 2, 1)
)
docsTestGroup.setObjects(
      *(("DOCS-TEST-MIB", "docsTestCapability"),
        ("DOCS-TEST-MIB", "docsTestStatus"),
        ("DOCS-TEST-MIB", "docsTestType"),
        ("DOCS-TEST-MIB", "docsTestData"),
        ("DOCS-TEST-MIB", "docsTestEnable"))
)
if mibBuilder.loadTexts:
    docsTestGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

docsTestBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 1, 12, 2, 1, 1)
)
if mibBuilder.loadTexts:
    docsTestBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOCS-TEST-MIB",
    **{"cableLabs": cableLabs,
       "clabFunction": clabFunction,
       "clabFuncMib2": clabFuncMib2,
       "clabFuncProprietary": clabFuncProprietary,
       "clabProject": clabProject,
       "clabProjDocsis": clabProjDocsis,
       "docsTestMIB": docsTestMIB,
       "docsTestMibObjects": docsTestMibObjects,
       "docsTestBaseObjects": docsTestBaseObjects,
       "docsTestCapability": docsTestCapability,
       "docsTestStatus": docsTestStatus,
       "docsTestSetupObjects": docsTestSetupObjects,
       "docsTestType": docsTestType,
       "docsTestData": docsTestData,
       "docsTestEnable": docsTestEnable,
       "docsTestConformance": docsTestConformance,
       "docsTestCompliances": docsTestCompliances,
       "docsTestBasicCompliance": docsTestBasicCompliance,
       "docsTestGroups": docsTestGroups,
       "docsTestGroup": docsTestGroup,
       "clabProjPacketCable": clabProjPacketCable,
       "clabProjOpenCable": clabProjOpenCable,
       "clabProjCableHome": clabProjCableHome}
)
