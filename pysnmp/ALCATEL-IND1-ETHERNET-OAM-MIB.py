# SNMP MIB module (ALCATEL-IND1-ETHERNET-OAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-ETHERNET-OAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:00 2024
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

(softentIND1EthernetOam,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1EthernetOam")

(Dot1agCfmMepId,
 Dot1agCfmMepIdOrZero,
 dot1agCfmMaIndex,
 dot1agCfmMdIndex,
 dot1agCfmMepEntry,
 dot1agCfmMepIdentifier) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmMepId",
    "Dot1agCfmMepIdOrZero",
    "dot1agCfmMaIndex",
    "dot1agCfmMdIndex",
    "dot1agCfmMepEntry",
    "dot1agCfmMepIdentifier")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

alcatelIND1EoamMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1)
)
alcatelIND1EoamMIB.setRevisions(
        ("2009-09-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1CfmMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1CfmMIBObjects = _AlcatelIND1CfmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1CfmMIBObjects.setStatus("current")
_AlaCfmBase_ObjectIdentity = ObjectIdentity
alaCfmBase = _AlaCfmBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 1)
)


class _AlaCfmGlobalClearStats_Type(Integer32):
    """Custom type alaCfmGlobalClearStats based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaCfmGlobalClearStats_Type.__name__ = "Integer32"
_AlaCfmGlobalClearStats_Object = MibScalar
alaCfmGlobalClearStats = _AlaCfmGlobalClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 1, 1),
    _AlaCfmGlobalClearStats_Type()
)
alaCfmGlobalClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaCfmGlobalClearStats.setStatus("current")


class _AlaCfmGlobalOWDClear_Type(Integer32):
    """Custom type alaCfmGlobalOWDClear based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaCfmGlobalOWDClear_Type.__name__ = "Integer32"
_AlaCfmGlobalOWDClear_Object = MibScalar
alaCfmGlobalOWDClear = _AlaCfmGlobalOWDClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 1, 2),
    _AlaCfmGlobalOWDClear_Type()
)
alaCfmGlobalOWDClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaCfmGlobalOWDClear.setStatus("current")


class _AlaCfmGlobalTWDClear_Type(Integer32):
    """Custom type alaCfmGlobalTWDClear based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaCfmGlobalTWDClear_Type.__name__ = "Integer32"
_AlaCfmGlobalTWDClear_Object = MibScalar
alaCfmGlobalTWDClear = _AlaCfmGlobalTWDClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 1, 3),
    _AlaCfmGlobalTWDClear_Type()
)
alaCfmGlobalTWDClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaCfmGlobalTWDClear.setStatus("current")
_AlaCfmMep_ObjectIdentity = ObjectIdentity
alaCfmMep = _AlaCfmMep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 2)
)
_AlaCfmMepTable_Object = MibTable
alaCfmMepTable = _AlaCfmMepTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alaCfmMepTable.setStatus("current")
_AlaCfmMepEntry_Object = MibTableRow
alaCfmMepEntry = _AlaCfmMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    alaCfmMepEntry.setStatus("current")


class _AlaCfmMepClearStats_Type(Integer32):
    """Custom type alaCfmMepClearStats based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaCfmMepClearStats_Type.__name__ = "Integer32"
_AlaCfmMepClearStats_Object = MibTableColumn
alaCfmMepClearStats = _AlaCfmMepClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 2, 1, 1, 1),
    _AlaCfmMepClearStats_Type()
)
alaCfmMepClearStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaCfmMepClearStats.setStatus("current")


class _AlaCfmMepOWDTMacAddress_Type(MacAddress):
    """Custom type alaCfmMepOWDTMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_AlaCfmMepOWDTMacAddress_Object = MibTableColumn
alaCfmMepOWDTMacAddress = _AlaCfmMepOWDTMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 2, 1, 1, 2),
    _AlaCfmMepOWDTMacAddress_Type()
)
alaCfmMepOWDTMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaCfmMepOWDTMacAddress.setStatus("current")
_AlaCfmMepOWDTRMepIdentifier_Type = Dot1agCfmMepId
_AlaCfmMepOWDTRMepIdentifier_Object = MibTableColumn
alaCfmMepOWDTRMepIdentifier = _AlaCfmMepOWDTRMepIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 2, 1, 1, 3),
    _AlaCfmMepOWDTRMepIdentifier_Type()
)
alaCfmMepOWDTRMepIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaCfmMepOWDTRMepIdentifier.setStatus("current")


class _AlaCfmMepOWDTPriority_Type(Unsigned32):
    """Custom type alaCfmMepOWDTPriority based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaCfmMepOWDTPriority_Type.__name__ = "Unsigned32"
_AlaCfmMepOWDTPriority_Object = MibTableColumn
alaCfmMepOWDTPriority = _AlaCfmMepOWDTPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 2, 1, 1, 4),
    _AlaCfmMepOWDTPriority_Type()
)
alaCfmMepOWDTPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaCfmMepOWDTPriority.setStatus("current")


class _AlaCfmMepTWDTMacAddress_Type(MacAddress):
    """Custom type alaCfmMepTWDTMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_AlaCfmMepTWDTMacAddress_Object = MibTableColumn
alaCfmMepTWDTMacAddress = _AlaCfmMepTWDTMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 2, 1, 1, 5),
    _AlaCfmMepTWDTMacAddress_Type()
)
alaCfmMepTWDTMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaCfmMepTWDTMacAddress.setStatus("current")
_AlaCfmMepTWDTRMepIdentifier_Type = Dot1agCfmMepId
_AlaCfmMepTWDTRMepIdentifier_Object = MibTableColumn
alaCfmMepTWDTRMepIdentifier = _AlaCfmMepTWDTRMepIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 2, 1, 1, 6),
    _AlaCfmMepTWDTRMepIdentifier_Type()
)
alaCfmMepTWDTRMepIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaCfmMepTWDTRMepIdentifier.setStatus("current")


class _AlaCfmMepTWDTPriority_Type(Unsigned32):
    """Custom type alaCfmMepTWDTPriority based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaCfmMepTWDTPriority_Type.__name__ = "Unsigned32"
_AlaCfmMepTWDTPriority_Object = MibTableColumn
alaCfmMepTWDTPriority = _AlaCfmMepTWDTPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 2, 1, 1, 7),
    _AlaCfmMepTWDTPriority_Type()
)
alaCfmMepTWDTPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaCfmMepTWDTPriority.setStatus("current")


class _AlaCfmMepRFPEnabled_Type(TruthValue):
    """Custom type alaCfmMepRFPEnabled based on TruthValue"""


_AlaCfmMepRFPEnabled_Object = MibTableColumn
alaCfmMepRFPEnabled = _AlaCfmMepRFPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 2, 1, 1, 8),
    _AlaCfmMepRFPEnabled_Type()
)
alaCfmMepRFPEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaCfmMepRFPEnabled.setStatus("current")


class _AlaCfmMepPortStatusTlv_Type(TruthValue):
    """Custom type alaCfmMepPortStatusTlv based on TruthValue"""


_AlaCfmMepPortStatusTlv_Object = MibTableColumn
alaCfmMepPortStatusTlv = _AlaCfmMepPortStatusTlv_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 2, 1, 1, 9),
    _AlaCfmMepPortStatusTlv_Type()
)
alaCfmMepPortStatusTlv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaCfmMepPortStatusTlv.setStatus("current")


class _AlaCfmMepIfStatusTlv_Type(TruthValue):
    """Custom type alaCfmMepIfStatusTlv based on TruthValue"""


_AlaCfmMepIfStatusTlv_Object = MibTableColumn
alaCfmMepIfStatusTlv = _AlaCfmMepIfStatusTlv_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 2, 1, 1, 10),
    _AlaCfmMepIfStatusTlv_Type()
)
alaCfmMepIfStatusTlv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaCfmMepIfStatusTlv.setStatus("current")
_AlaCfmDelayResult_ObjectIdentity = ObjectIdentity
alaCfmDelayResult = _AlaCfmDelayResult_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 3)
)
_AlaCfmDelayResultTable_Object = MibTable
alaCfmDelayResultTable = _AlaCfmDelayResultTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    alaCfmDelayResultTable.setStatus("current")
_AlaCfmDelayResultEntry_Object = MibTableRow
alaCfmDelayResultEntry = _AlaCfmDelayResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 3, 1, 1)
)
alaCfmDelayResultEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmDelayResultType"),
    (0, "ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmDelayResultRMepMacAddress"),
)
if mibBuilder.loadTexts:
    alaCfmDelayResultEntry.setStatus("current")


class _AlaCfmDelayResultType_Type(Integer32):
    """Custom type alaCfmDelayResultType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneWayTest", 1),
          ("twoWayTest", 2))
    )


_AlaCfmDelayResultType_Type.__name__ = "Integer32"
_AlaCfmDelayResultType_Object = MibTableColumn
alaCfmDelayResultType = _AlaCfmDelayResultType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 3, 1, 1, 1),
    _AlaCfmDelayResultType_Type()
)
alaCfmDelayResultType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaCfmDelayResultType.setStatus("current")
_AlaCfmDelayResultRMepMacAddress_Type = MacAddress
_AlaCfmDelayResultRMepMacAddress_Object = MibTableColumn
alaCfmDelayResultRMepMacAddress = _AlaCfmDelayResultRMepMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 3, 1, 1, 2),
    _AlaCfmDelayResultRMepMacAddress_Type()
)
alaCfmDelayResultRMepMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaCfmDelayResultRMepMacAddress.setStatus("current")
_AlaCfmDelayResultRMepIdentifier_Type = Dot1agCfmMepIdOrZero
_AlaCfmDelayResultRMepIdentifier_Object = MibTableColumn
alaCfmDelayResultRMepIdentifier = _AlaCfmDelayResultRMepIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 3, 1, 1, 3),
    _AlaCfmDelayResultRMepIdentifier_Type()
)
alaCfmDelayResultRMepIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCfmDelayResultRMepIdentifier.setStatus("current")
_AlaCfmDelayResultTestDelay_Type = Integer32
_AlaCfmDelayResultTestDelay_Object = MibTableColumn
alaCfmDelayResultTestDelay = _AlaCfmDelayResultTestDelay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 3, 1, 1, 4),
    _AlaCfmDelayResultTestDelay_Type()
)
alaCfmDelayResultTestDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCfmDelayResultTestDelay.setStatus("current")
if mibBuilder.loadTexts:
    alaCfmDelayResultTestDelay.setUnits("microseconds")
_AlaCfmDelayResultVariation_Type = Unsigned32
_AlaCfmDelayResultVariation_Object = MibTableColumn
alaCfmDelayResultVariation = _AlaCfmDelayResultVariation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 1, 3, 1, 1, 5),
    _AlaCfmDelayResultVariation_Type()
)
alaCfmDelayResultVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaCfmDelayResultVariation.setStatus("current")
if mibBuilder.loadTexts:
    alaCfmDelayResultVariation.setUnits("microseconds")
_AlaCfmConformance_ObjectIdentity = ObjectIdentity
alaCfmConformance = _AlaCfmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 2)
)
_AlaCfmGroups_ObjectIdentity = ObjectIdentity
alaCfmGroups = _AlaCfmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 2, 1)
)
_AlaCfmCompliances_ObjectIdentity = ObjectIdentity
alaCfmCompliances = _AlaCfmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 2, 2)
)
dot1agCfmMepEntry.registerAugmentions(
    ("ALCATEL-IND1-ETHERNET-OAM-MIB",
     "alaCfmMepEntry")
)
alaCfmMepEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())

# Managed Objects groups

alaCfmBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 2, 1, 1)
)
alaCfmBaseGroup.setObjects(
      *(("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmGlobalClearStats"),
        ("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmGlobalOWDClear"),
        ("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmGlobalTWDClear"))
)
if mibBuilder.loadTexts:
    alaCfmBaseGroup.setStatus("current")

alaCfmMepGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 2, 1, 2)
)
alaCfmMepGroup.setObjects(
      *(("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmMepClearStats"),
        ("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmMepOWDTMacAddress"),
        ("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmMepOWDTRMepIdentifier"),
        ("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmMepOWDTPriority"),
        ("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmMepTWDTMacAddress"),
        ("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmMepTWDTRMepIdentifier"),
        ("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmMepTWDTPriority"),
        ("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmMepRFPEnabled"))
)
if mibBuilder.loadTexts:
    alaCfmMepGroup.setStatus("current")

alaCfmDelayResultGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 2, 1, 3)
)
alaCfmDelayResultGroup.setObjects(
      *(("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmDelayResultRMepIdentifier"),
        ("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmDelayResultTestDelay"),
        ("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmDelayResultVariation"))
)
if mibBuilder.loadTexts:
    alaCfmDelayResultGroup.setStatus("current")

alaTlvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 2, 1, 4)
)
alaTlvGroup.setObjects(
      *(("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmMepPortStatusTlv"),
        ("ALCATEL-IND1-ETHERNET-OAM-MIB", "alaCfmMepIfStatusTlv"))
)
if mibBuilder.loadTexts:
    alaTlvGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alaCfmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 40, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alaCfmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-ETHERNET-OAM-MIB",
    **{"alcatelIND1EoamMIB": alcatelIND1EoamMIB,
       "alcatelIND1CfmMIBObjects": alcatelIND1CfmMIBObjects,
       "alaCfmBase": alaCfmBase,
       "alaCfmGlobalClearStats": alaCfmGlobalClearStats,
       "alaCfmGlobalOWDClear": alaCfmGlobalOWDClear,
       "alaCfmGlobalTWDClear": alaCfmGlobalTWDClear,
       "alaCfmMep": alaCfmMep,
       "alaCfmMepTable": alaCfmMepTable,
       "alaCfmMepEntry": alaCfmMepEntry,
       "alaCfmMepClearStats": alaCfmMepClearStats,
       "alaCfmMepOWDTMacAddress": alaCfmMepOWDTMacAddress,
       "alaCfmMepOWDTRMepIdentifier": alaCfmMepOWDTRMepIdentifier,
       "alaCfmMepOWDTPriority": alaCfmMepOWDTPriority,
       "alaCfmMepTWDTMacAddress": alaCfmMepTWDTMacAddress,
       "alaCfmMepTWDTRMepIdentifier": alaCfmMepTWDTRMepIdentifier,
       "alaCfmMepTWDTPriority": alaCfmMepTWDTPriority,
       "alaCfmMepRFPEnabled": alaCfmMepRFPEnabled,
       "alaCfmMepPortStatusTlv": alaCfmMepPortStatusTlv,
       "alaCfmMepIfStatusTlv": alaCfmMepIfStatusTlv,
       "alaCfmDelayResult": alaCfmDelayResult,
       "alaCfmDelayResultTable": alaCfmDelayResultTable,
       "alaCfmDelayResultEntry": alaCfmDelayResultEntry,
       "alaCfmDelayResultType": alaCfmDelayResultType,
       "alaCfmDelayResultRMepMacAddress": alaCfmDelayResultRMepMacAddress,
       "alaCfmDelayResultRMepIdentifier": alaCfmDelayResultRMepIdentifier,
       "alaCfmDelayResultTestDelay": alaCfmDelayResultTestDelay,
       "alaCfmDelayResultVariation": alaCfmDelayResultVariation,
       "alaCfmConformance": alaCfmConformance,
       "alaCfmGroups": alaCfmGroups,
       "alaCfmBaseGroup": alaCfmBaseGroup,
       "alaCfmMepGroup": alaCfmMepGroup,
       "alaCfmDelayResultGroup": alaCfmDelayResultGroup,
       "alaTlvGroup": alaTlvGroup,
       "alaCfmCompliances": alaCfmCompliances,
       "alaCfmCompliance": alaCfmCompliance}
)
