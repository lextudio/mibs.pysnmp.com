# SNMP MIB module (CTRON-SMARTTRUNK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-SMARTTRUNK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:37 2024
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

(ctSmartTrunkBranch,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctSmartTrunkBranch")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ctSmartTrunk = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CTSmartTrunkProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("decHuntGroup", 2),
          ("noProtocol", 1))
    )



class CTSmartTrunkIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class CTSmartTrunkName(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class CTSmartTrunkLoadBalanceType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("balancingUnspecified", 1),
          ("linkUtilization", 3),
          ("roundRobin", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CtSmartTrunkConfig_ObjectIdentity = ObjectIdentity
ctSmartTrunkConfig = _CtSmartTrunkConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1)
)
_CtTrunkGlobalStatus_Type = TruthValue
_CtTrunkGlobalStatus_Object = MibScalar
ctTrunkGlobalStatus = _CtTrunkGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 1),
    _CtTrunkGlobalStatus_Type()
)
ctTrunkGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctTrunkGlobalStatus.setStatus("current")
_CtTrunkConfigTable_Object = MibTable
ctTrunkConfigTable = _CtTrunkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ctTrunkConfigTable.setStatus("current")
_CtTrunkConfigEntry_Object = MibTableRow
ctTrunkConfigEntry = _CtTrunkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 3, 1)
)
ctTrunkConfigEntry.setIndexNames(
    (0, "CTRON-SMARTTRUNK-MIB", "ctTrunkIndex"),
)
if mibBuilder.loadTexts:
    ctTrunkConfigEntry.setStatus("current")
_CtTrunkIndex_Type = CTSmartTrunkIndex
_CtTrunkIndex_Object = MibTableColumn
ctTrunkIndex = _CtTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 3, 1, 1),
    _CtTrunkIndex_Type()
)
ctTrunkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctTrunkIndex.setStatus("current")
_CtTrunkConfigName_Type = CTSmartTrunkName
_CtTrunkConfigName_Object = MibTableColumn
ctTrunkConfigName = _CtTrunkConfigName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 3, 1, 2),
    _CtTrunkConfigName_Type()
)
ctTrunkConfigName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctTrunkConfigName.setStatus("current")


class _CtTrunkConfigProtocol_Type(CTSmartTrunkProtocol):
    """Custom type ctTrunkConfigProtocol based on CTSmartTrunkProtocol"""


_CtTrunkConfigProtocol_Object = MibTableColumn
ctTrunkConfigProtocol = _CtTrunkConfigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 3, 1, 3),
    _CtTrunkConfigProtocol_Type()
)
ctTrunkConfigProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctTrunkConfigProtocol.setStatus("current")


class _CtTrunkConfigLoadBalance_Type(CTSmartTrunkLoadBalanceType):
    """Custom type ctTrunkConfigLoadBalance based on CTSmartTrunkLoadBalanceType"""


_CtTrunkConfigLoadBalance_Object = MibTableColumn
ctTrunkConfigLoadBalance = _CtTrunkConfigLoadBalance_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 3, 1, 4),
    _CtTrunkConfigLoadBalance_Type()
)
ctTrunkConfigLoadBalance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctTrunkConfigLoadBalance.setStatus("current")
_CtTrunkIfIndex_Type = InterfaceIndex
_CtTrunkIfIndex_Object = MibTableColumn
ctTrunkIfIndex = _CtTrunkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 3, 1, 5),
    _CtTrunkIfIndex_Type()
)
ctTrunkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctTrunkIfIndex.setStatus("current")
_CtTrunkRowStatus_Type = RowStatus
_CtTrunkRowStatus_Object = MibTableColumn
ctTrunkRowStatus = _CtTrunkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 3, 1, 6),
    _CtTrunkRowStatus_Type()
)
ctTrunkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctTrunkRowStatus.setStatus("current")
_CtTrunkConnectionTable_Object = MibTable
ctTrunkConnectionTable = _CtTrunkConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ctTrunkConnectionTable.setStatus("current")
_CtTrunkConnectionEntry_Object = MibTableRow
ctTrunkConnectionEntry = _CtTrunkConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 4, 1)
)
ctTrunkConnectionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ctTrunkConnectionEntry.setStatus("current")
_CtTrunkPortRemoteIfIndex_Type = InterfaceIndex
_CtTrunkPortRemoteIfIndex_Object = MibTableColumn
ctTrunkPortRemoteIfIndex = _CtTrunkPortRemoteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 1, 4, 1, 1),
    _CtTrunkPortRemoteIfIndex_Type()
)
ctTrunkPortRemoteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctTrunkPortRemoteIfIndex.setStatus("current")
_CtSmartTrunkDebug_ObjectIdentity = ObjectIdentity
ctSmartTrunkDebug = _CtSmartTrunkDebug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 2)
)


class _CtTrunkLLAPRequirement_Type(Integer32):
    """Custom type ctTrunkLLAPRequirement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notRequired", 2),
          ("required", 1))
    )


_CtTrunkLLAPRequirement_Type.__name__ = "Integer32"
_CtTrunkLLAPRequirement_Object = MibScalar
ctTrunkLLAPRequirement = _CtTrunkLLAPRequirement_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 2, 1),
    _CtTrunkLLAPRequirement_Type()
)
ctTrunkLLAPRequirement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctTrunkLLAPRequirement.setStatus("current")
_CtTrunkMaxTrunks_Type = Integer32
_CtTrunkMaxTrunks_Object = MibScalar
ctTrunkMaxTrunks = _CtTrunkMaxTrunks_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 2, 2),
    _CtTrunkMaxTrunks_Type()
)
ctTrunkMaxTrunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctTrunkMaxTrunks.setStatus("current")
_CtTrunkFlowDiagnosticTable_Object = MibTable
ctTrunkFlowDiagnosticTable = _CtTrunkFlowDiagnosticTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 2, 4)
)
if mibBuilder.loadTexts:
    ctTrunkFlowDiagnosticTable.setStatus("current")
_CtTrunkFlowDiagnosticEntry_Object = MibTableRow
ctTrunkFlowDiagnosticEntry = _CtTrunkFlowDiagnosticEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 2, 4, 1)
)
ctTrunkFlowDiagnosticEntry.setIndexNames(
    (0, "CTRON-SMARTTRUNK-MIB", "ctTrunkIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ctTrunkFlowDiagnosticEntry.setStatus("current")
_CtTrunkFlowDiagnosticInstalledFlows_Type = Counter32
_CtTrunkFlowDiagnosticInstalledFlows_Object = MibTableColumn
ctTrunkFlowDiagnosticInstalledFlows = _CtTrunkFlowDiagnosticInstalledFlows_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 2, 4, 1, 1),
    _CtTrunkFlowDiagnosticInstalledFlows_Type()
)
ctTrunkFlowDiagnosticInstalledFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctTrunkFlowDiagnosticInstalledFlows.setStatus("current")
_CtTrunkConformance_ObjectIdentity = ObjectIdentity
ctTrunkConformance = _CtTrunkConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 3)
)
_CtTrunkCompliances_ObjectIdentity = ObjectIdentity
ctTrunkCompliances = _CtTrunkCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 3, 1)
)
_CtTrunkGroups_ObjectIdentity = ObjectIdentity
ctTrunkGroups = _CtTrunkGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 3, 2)
)

# Managed Objects groups

ctTrunkConfGroupV10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 3, 2, 1)
)
ctTrunkConfGroupV10.setObjects(
      *(("CTRON-SMARTTRUNK-MIB", "ctTrunkGlobalStatus"),
        ("CTRON-SMARTTRUNK-MIB", "ctTrunkRowStatus"),
        ("CTRON-SMARTTRUNK-MIB", "ctTrunkConfigName"),
        ("CTRON-SMARTTRUNK-MIB", "ctTrunkConfigProtocol"),
        ("CTRON-SMARTTRUNK-MIB", "ctTrunkConfigLoadBalance"),
        ("CTRON-SMARTTRUNK-MIB", "ctTrunkIfIndex"),
        ("CTRON-SMARTTRUNK-MIB", "ctTrunkPortRemoteIfIndex"),
        ("CTRON-SMARTTRUNK-MIB", "ctTrunkLLAPRequirement"),
        ("CTRON-SMARTTRUNK-MIB", "ctTrunkMaxTrunks"))
)
if mibBuilder.loadTexts:
    ctTrunkConfGroupV10.setStatus("current")

ctTrunkFlowDiagnosticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 3, 2, 2)
)
ctTrunkFlowDiagnosticGroup.setObjects(
    ("CTRON-SMARTTRUNK-MIB", "ctTrunkFlowDiagnosticInstalledFlows")
)
if mibBuilder.loadTexts:
    ctTrunkFlowDiagnosticGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ctTrunkComplianceV10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ctTrunkComplianceV10.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SMARTTRUNK-MIB",
    **{"CTSmartTrunkProtocol": CTSmartTrunkProtocol,
       "CTSmartTrunkIndex": CTSmartTrunkIndex,
       "CTSmartTrunkName": CTSmartTrunkName,
       "CTSmartTrunkLoadBalanceType": CTSmartTrunkLoadBalanceType,
       "ctSmartTrunk": ctSmartTrunk,
       "ctSmartTrunkConfig": ctSmartTrunkConfig,
       "ctTrunkGlobalStatus": ctTrunkGlobalStatus,
       "ctTrunkConfigTable": ctTrunkConfigTable,
       "ctTrunkConfigEntry": ctTrunkConfigEntry,
       "ctTrunkIndex": ctTrunkIndex,
       "ctTrunkConfigName": ctTrunkConfigName,
       "ctTrunkConfigProtocol": ctTrunkConfigProtocol,
       "ctTrunkConfigLoadBalance": ctTrunkConfigLoadBalance,
       "ctTrunkIfIndex": ctTrunkIfIndex,
       "ctTrunkRowStatus": ctTrunkRowStatus,
       "ctTrunkConnectionTable": ctTrunkConnectionTable,
       "ctTrunkConnectionEntry": ctTrunkConnectionEntry,
       "ctTrunkPortRemoteIfIndex": ctTrunkPortRemoteIfIndex,
       "ctSmartTrunkDebug": ctSmartTrunkDebug,
       "ctTrunkLLAPRequirement": ctTrunkLLAPRequirement,
       "ctTrunkMaxTrunks": ctTrunkMaxTrunks,
       "ctTrunkFlowDiagnosticTable": ctTrunkFlowDiagnosticTable,
       "ctTrunkFlowDiagnosticEntry": ctTrunkFlowDiagnosticEntry,
       "ctTrunkFlowDiagnosticInstalledFlows": ctTrunkFlowDiagnosticInstalledFlows,
       "ctTrunkConformance": ctTrunkConformance,
       "ctTrunkCompliances": ctTrunkCompliances,
       "ctTrunkComplianceV10": ctTrunkComplianceV10,
       "ctTrunkGroups": ctTrunkGroups,
       "ctTrunkConfGroupV10": ctTrunkConfGroupV10,
       "ctTrunkFlowDiagnosticGroup": ctTrunkFlowDiagnosticGroup}
)
