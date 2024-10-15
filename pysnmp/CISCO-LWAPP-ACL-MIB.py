# SNMP MIB module (CISCO-LWAPP-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-ACL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:10 2024
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

ciscoLwappAclMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 577)
)
ciscoLwappAclMIB.setRevisions(
        ("2010-03-04 00:00",
         "2006-08-29 00:00",
         "2006-07-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappAclMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappAclMIBNotifs = _CiscoLwappAclMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 0)
)
_CiscoLwappAclMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappAclMIBObjects = _CiscoLwappAclMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1)
)
_CiscoLwappCpuAcl_ObjectIdentity = ObjectIdentity
ciscoLwappCpuAcl = _CiscoLwappCpuAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 1)
)
_ClaCpuAclTable_Object = MibTable
claCpuAclTable = _ClaCpuAclTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 1, 1)
)
if mibBuilder.loadTexts:
    claCpuAclTable.setStatus("current")
_ClaCpuAclEntry_Object = MibTableRow
claCpuAclEntry = _ClaCpuAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 1, 1, 1)
)
claCpuAclEntry.setIndexNames(
    (0, "CISCO-LWAPP-ACL-MIB", "claCpuAclIndex"),
)
if mibBuilder.loadTexts:
    claCpuAclEntry.setStatus("current")
_ClaCpuAclIndex_Type = Unsigned32
_ClaCpuAclIndex_Object = MibTableColumn
claCpuAclIndex = _ClaCpuAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 1, 1, 1, 1),
    _ClaCpuAclIndex_Type()
)
claCpuAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    claCpuAclIndex.setStatus("current")


class _ClaCpuAclName_Type(DisplayString):
    """Custom type claCpuAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ClaCpuAclName_Type.__name__ = "DisplayString"
_ClaCpuAclName_Object = MibTableColumn
claCpuAclName = _ClaCpuAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 1, 1, 1, 2),
    _ClaCpuAclName_Type()
)
claCpuAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claCpuAclName.setStatus("current")


class _ClaCpuAclPacketApplicability_Type(Integer32):
    """Custom type claCpuAclPacketApplicability based on Integer32"""
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
        *(("both", 4),
          ("none", 1),
          ("wired", 2),
          ("wireless", 3))
    )


_ClaCpuAclPacketApplicability_Type.__name__ = "Integer32"
_ClaCpuAclPacketApplicability_Object = MibTableColumn
claCpuAclPacketApplicability = _ClaCpuAclPacketApplicability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 1, 1, 1, 3),
    _ClaCpuAclPacketApplicability_Type()
)
claCpuAclPacketApplicability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claCpuAclPacketApplicability.setStatus("current")
_CiscoLwappControllerAcl_ObjectIdentity = ObjectIdentity
ciscoLwappControllerAcl = _CiscoLwappControllerAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2)
)
_ClaAclTable_Object = MibTable
claAclTable = _ClaAclTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2, 1)
)
if mibBuilder.loadTexts:
    claAclTable.setStatus("current")
_ClaAclEntry_Object = MibTableRow
claAclEntry = _ClaAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2, 1, 1)
)
claAclEntry.setIndexNames(
    (0, "CISCO-LWAPP-ACL-MIB", "claAclName"),
)
if mibBuilder.loadTexts:
    claAclEntry.setStatus("current")


class _ClaAclName_Type(OctetString):
    """Custom type claAclName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ClaAclName_Type.__name__ = "OctetString"
_ClaAclName_Object = MibTableColumn
claAclName = _ClaAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2, 1, 1, 1),
    _ClaAclName_Type()
)
claAclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    claAclName.setStatus("current")
_ClaAclCounterClear_Type = TruthValue
_ClaAclCounterClear_Object = MibTableColumn
claAclCounterClear = _ClaAclCounterClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2, 1, 1, 2),
    _ClaAclCounterClear_Type()
)
claAclCounterClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claAclCounterClear.setStatus("current")
_ClaAclRuleTable_Object = MibTable
claAclRuleTable = _ClaAclRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2, 2)
)
if mibBuilder.loadTexts:
    claAclRuleTable.setStatus("current")
_ClaAclRuleEntry_Object = MibTableRow
claAclRuleEntry = _ClaAclRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2, 2, 1)
)
claAclRuleEntry.setIndexNames(
    (0, "CISCO-LWAPP-ACL-MIB", "claAclName"),
    (0, "CISCO-LWAPP-ACL-MIB", "claAclRuleIndex"),
)
if mibBuilder.loadTexts:
    claAclRuleEntry.setStatus("current")


class _ClaAclRuleIndex_Type(Unsigned32):
    """Custom type claAclRuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_ClaAclRuleIndex_Type.__name__ = "Unsigned32"
_ClaAclRuleIndex_Object = MibTableColumn
claAclRuleIndex = _ClaAclRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2, 2, 1, 2),
    _ClaAclRuleIndex_Type()
)
claAclRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    claAclRuleIndex.setStatus("current")
_ClaAclRuleHits_Type = Counter32
_ClaAclRuleHits_Object = MibTableColumn
claAclRuleHits = _ClaAclRuleHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2, 2, 1, 3),
    _ClaAclRuleHits_Type()
)
claAclRuleHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    claAclRuleHits.setStatus("current")
_CiscoLwappControllerAclGeneral_ObjectIdentity = ObjectIdentity
ciscoLwappControllerAclGeneral = _CiscoLwappControllerAclGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 3)
)


class _ClaAclCounterEnable_Type(TruthValue):
    """Custom type claAclCounterEnable based on TruthValue"""


_ClaAclCounterEnable_Object = MibScalar
claAclCounterEnable = _ClaAclCounterEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 3, 1),
    _ClaAclCounterEnable_Type()
)
claAclCounterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claAclCounterEnable.setStatus("current")
_CiscoLwappAclMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappAclMIBConform = _CiscoLwappAclMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 2)
)
_CiscoLwappAclMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappAclMIBCompliances = _CiscoLwappAclMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 2, 1)
)
_CiscoLwappAclMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappAclMIBGroups = _CiscoLwappAclMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 2, 2)
)

# Managed Objects groups

ciscoLwappCpuAclGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 2, 2, 1)
)
ciscoLwappCpuAclGroup.setObjects(
      *(("CISCO-LWAPP-ACL-MIB", "claCpuAclName"),
        ("CISCO-LWAPP-ACL-MIB", "claCpuAclPacketApplicability"))
)
if mibBuilder.loadTexts:
    ciscoLwappCpuAclGroup.setStatus("current")

ciscoLwappAclGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 2, 2, 2)
)
ciscoLwappAclGroup.setObjects(
      *(("CISCO-LWAPP-ACL-MIB", "claAclCounterEnable"),
        ("CISCO-LWAPP-ACL-MIB", "claAclCounterClear"),
        ("CISCO-LWAPP-ACL-MIB", "claAclRuleHits"))
)
if mibBuilder.loadTexts:
    ciscoLwappAclGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLwappAclMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappAclMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappAclMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoLwappAclMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-ACL-MIB",
    **{"ciscoLwappAclMIB": ciscoLwappAclMIB,
       "ciscoLwappAclMIBNotifs": ciscoLwappAclMIBNotifs,
       "ciscoLwappAclMIBObjects": ciscoLwappAclMIBObjects,
       "ciscoLwappCpuAcl": ciscoLwappCpuAcl,
       "claCpuAclTable": claCpuAclTable,
       "claCpuAclEntry": claCpuAclEntry,
       "claCpuAclIndex": claCpuAclIndex,
       "claCpuAclName": claCpuAclName,
       "claCpuAclPacketApplicability": claCpuAclPacketApplicability,
       "ciscoLwappControllerAcl": ciscoLwappControllerAcl,
       "claAclTable": claAclTable,
       "claAclEntry": claAclEntry,
       "claAclName": claAclName,
       "claAclCounterClear": claAclCounterClear,
       "claAclRuleTable": claAclRuleTable,
       "claAclRuleEntry": claAclRuleEntry,
       "claAclRuleIndex": claAclRuleIndex,
       "claAclRuleHits": claAclRuleHits,
       "ciscoLwappControllerAclGeneral": ciscoLwappControllerAclGeneral,
       "claAclCounterEnable": claAclCounterEnable,
       "ciscoLwappAclMIBConform": ciscoLwappAclMIBConform,
       "ciscoLwappAclMIBCompliances": ciscoLwappAclMIBCompliances,
       "ciscoLwappAclMIBCompliance": ciscoLwappAclMIBCompliance,
       "ciscoLwappAclMIBComplianceRev1": ciscoLwappAclMIBComplianceRev1,
       "ciscoLwappAclMIBGroups": ciscoLwappAclMIBGroups,
       "ciscoLwappCpuAclGroup": ciscoLwappCpuAclGroup,
       "ciscoLwappAclGroup": ciscoLwappAclGroup}
)
