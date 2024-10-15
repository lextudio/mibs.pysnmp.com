# SNMP MIB module (POLICY-FRAMEWORK-PIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/POLICY-FRAMEWORK-PIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:39 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(policy,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "policy")


# MODULE-IDENTITY

policyFrameworkPib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 1)
)
policyFrameworkPib.setRevisions(
        ("2004-07-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Role(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class RoleCombination(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class PolicyInstanceId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



# MIB Managed Objects in the order of their OIDs

_PolicyBasePibClass_ObjectIdentity = ObjectIdentity
policyBasePibClass = _PolicyBasePibClass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 1, 1)
)
_PolicyPrcSupportTable_Object = MibTable
policyPrcSupportTable = _PolicyPrcSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    policyPrcSupportTable.setStatus("current")
_PolicyPrcSupportEntry_Object = MibTableRow
policyPrcSupportEntry = _PolicyPrcSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 1, 1)
)
policyPrcSupportEntry.setIndexNames(
    (0, "POLICY-FRAMEWORK-PIB", "policyPrcSupportPrid"),
)
if mibBuilder.loadTexts:
    policyPrcSupportEntry.setStatus("current")
_PolicyPrcSupportPrid_Type = PolicyInstanceId
_PolicyPrcSupportPrid_Object = MibTableColumn
policyPrcSupportPrid = _PolicyPrcSupportPrid_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 1, 1, 1),
    _PolicyPrcSupportPrid_Type()
)
policyPrcSupportPrid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyPrcSupportPrid.setStatus("current")
_PolicyPrcSupportSupportedPrc_Type = ObjectIdentifier
_PolicyPrcSupportSupportedPrc_Object = MibTableColumn
policyPrcSupportSupportedPrc = _PolicyPrcSupportSupportedPrc_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 1, 1, 2),
    _PolicyPrcSupportSupportedPrc_Type()
)
policyPrcSupportSupportedPrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyPrcSupportSupportedPrc.setStatus("current")
_PolicyPrcSupportSupportedAttrs_Type = OctetString
_PolicyPrcSupportSupportedAttrs_Object = MibTableColumn
policyPrcSupportSupportedAttrs = _PolicyPrcSupportSupportedAttrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 1, 1, 3),
    _PolicyPrcSupportSupportedAttrs_Type()
)
policyPrcSupportSupportedAttrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyPrcSupportSupportedAttrs.setStatus("current")
_PolicyPrcSupportMaxPris_Type = Unsigned32
_PolicyPrcSupportMaxPris_Object = MibTableColumn
policyPrcSupportMaxPris = _PolicyPrcSupportMaxPris_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 1, 1, 4),
    _PolicyPrcSupportMaxPris_Type()
)
policyPrcSupportMaxPris.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyPrcSupportMaxPris.setStatus("current")
_PolicyPibIncarnationTable_Object = MibTable
policyPibIncarnationTable = _PolicyPibIncarnationTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    policyPibIncarnationTable.setStatus("current")
_PolicyPibIncarnationEntry_Object = MibTableRow
policyPibIncarnationEntry = _PolicyPibIncarnationEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 2, 1)
)
policyPibIncarnationEntry.setIndexNames(
    (0, "POLICY-FRAMEWORK-PIB", "policyPibIncarnationPrid"),
)
if mibBuilder.loadTexts:
    policyPibIncarnationEntry.setStatus("current")
_PolicyPibIncarnationPrid_Type = PolicyInstanceId
_PolicyPibIncarnationPrid_Object = MibTableColumn
policyPibIncarnationPrid = _PolicyPibIncarnationPrid_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 2, 1, 1),
    _PolicyPibIncarnationPrid_Type()
)
policyPibIncarnationPrid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyPibIncarnationPrid.setStatus("current")
_PolicyPibIncarnationName_Type = SnmpAdminString
_PolicyPibIncarnationName_Object = MibTableColumn
policyPibIncarnationName = _PolicyPibIncarnationName_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 2, 1, 2),
    _PolicyPibIncarnationName_Type()
)
policyPibIncarnationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyPibIncarnationName.setStatus("current")
_PolicyPibIncarnationId_Type = OctetString
_PolicyPibIncarnationId_Object = MibTableColumn
policyPibIncarnationId = _PolicyPibIncarnationId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 2, 1, 3),
    _PolicyPibIncarnationId_Type()
)
policyPibIncarnationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyPibIncarnationId.setStatus("current")


class _PolicyPibIncarnationLongevity_Type(Integer32):
    """Custom type policyPibIncarnationLongevity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("expireImmediate", 2),
          ("expireNever", 1),
          ("expireOnTimeout", 3))
    )


_PolicyPibIncarnationLongevity_Type.__name__ = "Integer32"
_PolicyPibIncarnationLongevity_Object = MibTableColumn
policyPibIncarnationLongevity = _PolicyPibIncarnationLongevity_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 2, 1, 4),
    _PolicyPibIncarnationLongevity_Type()
)
policyPibIncarnationLongevity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyPibIncarnationLongevity.setStatus("current")
_PolicyPibIncarnationTtl_Type = Unsigned32
_PolicyPibIncarnationTtl_Object = MibTableColumn
policyPibIncarnationTtl = _PolicyPibIncarnationTtl_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 2, 1, 5),
    _PolicyPibIncarnationTtl_Type()
)
policyPibIncarnationTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyPibIncarnationTtl.setStatus("current")
_PolicyPibIncarnationActive_Type = TruthValue
_PolicyPibIncarnationActive_Object = MibTableColumn
policyPibIncarnationActive = _PolicyPibIncarnationActive_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 2, 1, 6),
    _PolicyPibIncarnationActive_Type()
)
policyPibIncarnationActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyPibIncarnationActive.setStatus("current")
_PolicyDeviceIdentificationTable_Object = MibTable
policyDeviceIdentificationTable = _PolicyDeviceIdentificationTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    policyDeviceIdentificationTable.setStatus("current")
_PolicyDeviceIdentificationEntry_Object = MibTableRow
policyDeviceIdentificationEntry = _PolicyDeviceIdentificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 3, 1)
)
policyDeviceIdentificationEntry.setIndexNames(
    (0, "POLICY-FRAMEWORK-PIB", "policyDeviceIdentificationPrid"),
)
if mibBuilder.loadTexts:
    policyDeviceIdentificationEntry.setStatus("current")
_PolicyDeviceIdentificationPrid_Type = PolicyInstanceId
_PolicyDeviceIdentificationPrid_Object = MibTableColumn
policyDeviceIdentificationPrid = _PolicyDeviceIdentificationPrid_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 3, 1, 1),
    _PolicyDeviceIdentificationPrid_Type()
)
policyDeviceIdentificationPrid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyDeviceIdentificationPrid.setStatus("current")


class _PolicyDeviceIdentificationDescr_Type(SnmpAdminString):
    """Custom type policyDeviceIdentificationDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PolicyDeviceIdentificationDescr_Type.__name__ = "SnmpAdminString"
_PolicyDeviceIdentificationDescr_Object = MibTableColumn
policyDeviceIdentificationDescr = _PolicyDeviceIdentificationDescr_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 3, 1, 2),
    _PolicyDeviceIdentificationDescr_Type()
)
policyDeviceIdentificationDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyDeviceIdentificationDescr.setStatus("current")
_PolicyDeviceIdentificationMaxMsg_Type = Unsigned32
_PolicyDeviceIdentificationMaxMsg_Object = MibTableColumn
policyDeviceIdentificationMaxMsg = _PolicyDeviceIdentificationMaxMsg_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 3, 1, 3),
    _PolicyDeviceIdentificationMaxMsg_Type()
)
policyDeviceIdentificationMaxMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyDeviceIdentificationMaxMsg.setStatus("current")
_PolicyCompLimitsTable_Object = MibTable
policyCompLimitsTable = _PolicyCompLimitsTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 4)
)
if mibBuilder.loadTexts:
    policyCompLimitsTable.setStatus("current")
_PolicyCompLimitsEntry_Object = MibTableRow
policyCompLimitsEntry = _PolicyCompLimitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 4, 1)
)
policyCompLimitsEntry.setIndexNames(
    (0, "POLICY-FRAMEWORK-PIB", "policyCompLimitsPrid"),
)
if mibBuilder.loadTexts:
    policyCompLimitsEntry.setStatus("current")
_PolicyCompLimitsPrid_Type = PolicyInstanceId
_PolicyCompLimitsPrid_Object = MibTableColumn
policyCompLimitsPrid = _PolicyCompLimitsPrid_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 4, 1, 1),
    _PolicyCompLimitsPrid_Type()
)
policyCompLimitsPrid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    policyCompLimitsPrid.setStatus("current")
_PolicyCompLimitsComponent_Type = ObjectIdentifier
_PolicyCompLimitsComponent_Object = MibTableColumn
policyCompLimitsComponent = _PolicyCompLimitsComponent_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 4, 1, 2),
    _PolicyCompLimitsComponent_Type()
)
policyCompLimitsComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyCompLimitsComponent.setStatus("current")
_PolicyCompLimitsType_Type = Integer32
_PolicyCompLimitsType_Object = MibTableColumn
policyCompLimitsType = _PolicyCompLimitsType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 4, 1, 3),
    _PolicyCompLimitsType_Type()
)
policyCompLimitsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyCompLimitsType.setStatus("current")


class _PolicyCompLimitsGuidance_Type(OctetString):
    """Custom type policyCompLimitsGuidance based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PolicyCompLimitsGuidance_Type.__name__ = "OctetString"
_PolicyCompLimitsGuidance_Object = MibTableColumn
policyCompLimitsGuidance = _PolicyCompLimitsGuidance_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 1, 1, 4, 1, 4),
    _PolicyCompLimitsGuidance_Type()
)
policyCompLimitsGuidance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyCompLimitsGuidance.setStatus("current")
_PolicyBasePibConformance_ObjectIdentity = ObjectIdentity
policyBasePibConformance = _PolicyBasePibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 1, 2)
)
_PolicyBasePibCompliances_ObjectIdentity = ObjectIdentity
policyBasePibCompliances = _PolicyBasePibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 1, 2, 1)
)
_PolicyBasePibGroups_ObjectIdentity = ObjectIdentity
policyBasePibGroups = _PolicyBasePibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 1, 2, 2)
)

# Managed Objects groups

policyPrcSupportGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 1, 2, 2, 1)
)
policyPrcSupportGroup.setObjects(
      *(("POLICY-FRAMEWORK-PIB", "policyPrcSupportSupportedPrc"),
        ("POLICY-FRAMEWORK-PIB", "policyPrcSupportSupportedAttrs"),
        ("POLICY-FRAMEWORK-PIB", "policyPrcSupportMaxPris"))
)
if mibBuilder.loadTexts:
    policyPrcSupportGroup.setStatus("current")

policyPibIncarnationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 1, 2, 2, 2)
)
policyPibIncarnationGroup.setObjects(
      *(("POLICY-FRAMEWORK-PIB", "policyPibIncarnationName"),
        ("POLICY-FRAMEWORK-PIB", "policyPibIncarnationId"),
        ("POLICY-FRAMEWORK-PIB", "policyPibIncarnationLongevity"),
        ("POLICY-FRAMEWORK-PIB", "policyPibIncarnationTtl"),
        ("POLICY-FRAMEWORK-PIB", "policyPibIncarnationActive"))
)
if mibBuilder.loadTexts:
    policyPibIncarnationGroup.setStatus("current")

policyDeviceIdentificationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 1, 2, 2, 3)
)
policyDeviceIdentificationGroup.setObjects(
      *(("POLICY-FRAMEWORK-PIB", "policyDeviceIdentificationDescr"),
        ("POLICY-FRAMEWORK-PIB", "policyDeviceIdentificationMaxMsg"))
)
if mibBuilder.loadTexts:
    policyDeviceIdentificationGroup.setStatus("current")

policyCompLimitsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 1, 2, 2, 4)
)
policyCompLimitsGroup.setObjects(
      *(("POLICY-FRAMEWORK-PIB", "policyCompLimitsComponent"),
        ("POLICY-FRAMEWORK-PIB", "policyCompLimitsType"),
        ("POLICY-FRAMEWORK-PIB", "policyCompLimitsGuidance"))
)
if mibBuilder.loadTexts:
    policyCompLimitsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

policyBasePibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 45, 4, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    policyBasePibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "POLICY-FRAMEWORK-PIB",
    **{"Role": Role,
       "RoleCombination": RoleCombination,
       "PolicyInstanceId": PolicyInstanceId,
       "policyFrameworkPib": policyFrameworkPib,
       "policyBasePibClass": policyBasePibClass,
       "policyPrcSupportTable": policyPrcSupportTable,
       "policyPrcSupportEntry": policyPrcSupportEntry,
       "policyPrcSupportPrid": policyPrcSupportPrid,
       "policyPrcSupportSupportedPrc": policyPrcSupportSupportedPrc,
       "policyPrcSupportSupportedAttrs": policyPrcSupportSupportedAttrs,
       "policyPrcSupportMaxPris": policyPrcSupportMaxPris,
       "policyPibIncarnationTable": policyPibIncarnationTable,
       "policyPibIncarnationEntry": policyPibIncarnationEntry,
       "policyPibIncarnationPrid": policyPibIncarnationPrid,
       "policyPibIncarnationName": policyPibIncarnationName,
       "policyPibIncarnationId": policyPibIncarnationId,
       "policyPibIncarnationLongevity": policyPibIncarnationLongevity,
       "policyPibIncarnationTtl": policyPibIncarnationTtl,
       "policyPibIncarnationActive": policyPibIncarnationActive,
       "policyDeviceIdentificationTable": policyDeviceIdentificationTable,
       "policyDeviceIdentificationEntry": policyDeviceIdentificationEntry,
       "policyDeviceIdentificationPrid": policyDeviceIdentificationPrid,
       "policyDeviceIdentificationDescr": policyDeviceIdentificationDescr,
       "policyDeviceIdentificationMaxMsg": policyDeviceIdentificationMaxMsg,
       "policyCompLimitsTable": policyCompLimitsTable,
       "policyCompLimitsEntry": policyCompLimitsEntry,
       "policyCompLimitsPrid": policyCompLimitsPrid,
       "policyCompLimitsComponent": policyCompLimitsComponent,
       "policyCompLimitsType": policyCompLimitsType,
       "policyCompLimitsGuidance": policyCompLimitsGuidance,
       "policyBasePibConformance": policyBasePibConformance,
       "policyBasePibCompliances": policyBasePibCompliances,
       "policyBasePibCompliance": policyBasePibCompliance,
       "policyBasePibGroups": policyBasePibGroups,
       "policyPrcSupportGroup": policyPrcSupportGroup,
       "policyPibIncarnationGroup": policyPibIncarnationGroup,
       "policyDeviceIdentificationGroup": policyDeviceIdentificationGroup,
       "policyCompLimitsGroup": policyCompLimitsGroup}
)
